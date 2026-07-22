"""
Font generation pipeline using DeepVecFont-v2.
"""

import os
import json
from flask import Blueprint, request, jsonify, current_app
from threading import Thread
import logging
from datetime import datetime
from backend.models.deepvecfont_v2 import get_model, generate_fonts_task
from backend.utils.image_processor import preprocess_font_sample, validate_image, validate_font

logger = logging.getLogger(__name__)

generate_bp = Blueprint('generate', __name__, url_prefix='/api')

# Store generation tasks
generation_tasks = {}


@generate_bp.route('/generate', methods=['POST'])
def generate_fonts():
    """
    Generate fonts using DeepVecFont-v2.
    
    Request:
    - task_id: ID from upload (required)
    - language: target language code (required)
    - n_samples: number of candidates to generate (default: 20)
    - reference_char_ids: list of reference character indices (optional)
    
    Response:
    - generation_id: unique generation task ID
    - status: processing status
    - estimated_time: estimated completion time
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        task_id = data.get('task_id')
        language = data.get('language')
        n_samples = data.get('n_samples', 20)
        reference_char_ids = data.get('reference_char_ids', [])
        
        if not task_id or not language:
            return jsonify({'error': 'task_id and language are required'}), 400
        
        # Validate file exists
        upload_folder = current_app.config['UPLOAD_FOLDER']
        file_exists = False
        input_file = None
        
        for filename in os.listdir(upload_folder):
            if filename.startswith(task_id):
                input_file = os.path.join(upload_folder, filename)
                file_exists = True
                break
        
        if not file_exists:
            return jsonify({'error': f'File for task {task_id} not found'}), 404
        
        # Validate input file
        file_ext = os.path.splitext(input_file)[1].lower()
        if file_ext in ['.ttf', '.otf']:
            if not validate_font(input_file):
                return jsonify({'error': 'Invalid font file'}), 400
        elif file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            if not validate_image(input_file):
                return jsonify({'error': 'Invalid image file'}), 400
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
        
        # Create generation task
        generation_id = task_id  # Use same ID for tracking
        generation_tasks[generation_id] = {
            'status': 'queued',
            'created_at': datetime.now().isoformat(),
            'language': language,
            'n_samples': n_samples,
            'progress': 0,
            'results': None,
            'error': None
        }
        
        # Start generation in background thread
        thread = Thread(
            target=_process_generation,
            args=(generation_id, input_file, language, n_samples, reference_char_ids, current_app.config['RESULTS_FOLDER'])
        )
        thread.daemon = True
        thread.start()
        
        logger.info(f"Generation started: {generation_id} for language {language}")
        
        return jsonify({
            'success': True,
            'generation_id': generation_id,
            'task_id': task_id,
            'language': language,
            'status': 'processing',
            'n_samples': n_samples,
            'estimated_time_seconds': 300,
            'check_status_url': f'/api/generate/status/{generation_id}'
        }), 202
    
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500


def _process_generation(generation_id, input_file, language, n_samples, reference_char_ids, results_folder):
    """
    Background process for font generation using DeepVecFont-v2.
    
    Pipeline:
    1. Load and preprocess input (TTF/image)
    2. Load DeepVecFont-v2 model for target language
    3. Download model checkpoint if needed
    4. Run inference to generate font candidates
    5. Select best using IOU metric
    6. Render SVG outputs
    7. Save results
    """
    try:
        task = generation_tasks[generation_id]
        task['status'] = 'processing'
        task['progress'] = 5
        
        logger.info(f"[{generation_id}] Starting font generation pipeline...")
        
        # Step 1: Preprocess input
        logger.info(f"[{generation_id}] Preprocessing input file...")
        task['progress'] = 10
        
        try:
            input_data = preprocess_font_sample(input_file, language)
            if input_data is None:
                raise ValueError("Failed to preprocess input file")
        except Exception as e:
            logger.error(f"[{generation_id}] Preprocessing error: {e}")
            task['status'] = 'failed'
            task['error'] = f'Preprocessing error: {str(e)}'
            return
        
        task['progress'] = 20
        
        # Step 2: Initialize and load model
        logger.info(f"[{generation_id}] Loading DeepVecFont-v2 model for {language}...")
        task['progress'] = 30
        
        try:
            model = get_model()
            if not model.load_checkpoint(language):
                raise ValueError(f"Failed to load model checkpoint for {language}")
        except Exception as e:
            logger.error(f"[{generation_id}] Model loading error: {e}")
            task['status'] = 'failed'
            task['error'] = f'Model loading error: {str(e)}'
            return
        
        task['progress'] = 40
        
        # Step 3: Generate fonts
        logger.info(f"[{generation_id}] Generating {n_samples} font candidates...")
        task['progress'] = 50
        
        try:
            generation_results = generate_fonts_task(
                input_data,
                language=language,
                n_samples=n_samples,
                reference_chars=reference_char_ids if reference_char_ids else None
            )
            
            if generation_results is None:
                raise ValueError("Font generation failed")
        except Exception as e:
            logger.error(f"[{generation_id}] Generation error: {e}")
            task['status'] = 'failed'
            task['error'] = f'Generation error: {str(e)}'
            return
        
        task['progress'] = 80
        
        # Step 4: Save results
        logger.info(f"[{generation_id}] Saving results...")
        task['progress'] = 85
        
        try:
            results_output_dir = os.path.join(results_folder, 'fonts', generation_id)
            os.makedirs(results_output_dir, exist_ok=True)
            
            # Save SVG outputs
            svg_files = model.save_svg_output(
                generation_results['svg_outputs'],
                results_output_dir,
                language
            )
            
            # Save metadata
            metadata = {
                'generation_id': generation_id,
                'language': language,
                'n_samples': n_samples,
                'svg_files': svg_files,
                'candidates': generation_results.get('candidates', {}),
                'metadata': generation_results.get('metadata', {}),
                'generated_at': datetime.now().isoformat()
            }
            
            metadata_path = os.path.join(results_output_dir, 'metadata.json')
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            logger.info(f"[{generation_id}] Saved {len(svg_files)} SVG files and metadata")
        
        except Exception as e:
            logger.error(f"[{generation_id}] Error saving results: {e}")
            task['status'] = 'failed'
            task['error'] = f'Error saving results: {str(e)}'
            return
        
        task['progress'] = 90
        
        # Step 5: Store final results
        task['results'] = {
            'generation_id': generation_id,
            'language': language,
            'n_samples': len(svg_files),
            'output_folder': results_output_dir,
            'files': svg_files,
            'metadata_file': metadata_path,
            'preview_url': f'/api/results/{generation_id}'
        }
        
        task['status'] = 'completed'
        task['progress'] = 100
        task['completed_at'] = datetime.now().isoformat()
        
        logger.info(f"[{generation_id}] ✓ Font generation completed successfully!")
    
    except Exception as e:
        logger.error(f"[{generation_id}] Unexpected error: {str(e)}")
        task['status'] = 'failed'
        task['error'] = f'Unexpected error: {str(e)}'


@generate_bp.route('/generate/status/<generation_id>', methods=['GET'])
def generation_status(generation_id):
    """
    Check the status of a font generation task.
    """
    try:
        if generation_id not in generation_tasks:
            return jsonify({'error': f'Generation task {generation_id} not found'}), 404
        
        task = generation_tasks[generation_id]
        response = {
            'generation_id': generation_id,
            'status': task['status'],
            'progress': task['progress'],
            'created_at': task['created_at']
        }
        
        if task.get('completed_at'):
            response['completed_at'] = task['completed_at']
        
        if task.get('error'):
            response['error'] = task['error']
        
        if task['status'] == 'completed' and task.get('results'):
            response['results'] = task['results']
        
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Status check error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@generate_bp.route('/generate/list', methods=['GET'])
def list_generations():
    """
    List all generation tasks.
    """
    try:
        tasks = []
        for gen_id, task in generation_tasks.items():
            tasks.append({
                'generation_id': gen_id,
                'status': task['status'],
                'language': task['language'],
                'created_at': task['created_at'],
                'progress': task['progress'],
                'n_samples': task.get('results', {}).get('n_samples', 0)
            })
        
        return jsonify({
            'total': len(tasks),
            'tasks': tasks
        }), 200
    
    except Exception as e:
        logger.error(f"List error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@generate_bp.route('/generate/cancel/<generation_id>', methods=['POST'])
def cancel_generation(generation_id):
    """
    Cancel an ongoing generation task.
    """
    try:
        if generation_id not in generation_tasks:
            return jsonify({'error': f'Generation task {generation_id} not found'}), 404
        
        task = generation_tasks[generation_id]
        
        if task['status'] in ['completed', 'failed', 'cancelled']:
            return jsonify({'error': f'Cannot cancel task with status: {task["status"]}'}), 400
        
        task['status'] = 'cancelled'
        task['error'] = 'Cancelled by user'
        
        logger.info(f"Generation task cancelled: {generation_id}")
        
        return jsonify({
            'success': True,
            'generation_id': generation_id,
            'status': 'cancelled'
        }), 200
    
    except Exception as e:
        logger.error(f"Cancellation error: {str(e)}")
        return jsonify({'error': str(e)}), 500
