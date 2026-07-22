"""
Font generation pipeline using DeepVecFont-v2.
"""

import os
import json
from flask import Blueprint, request, jsonify, current_app
from threading import Thread
import logging
from datetime import datetime

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
            args=(generation_id, input_file, language, n_samples, reference_char_ids)
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
            'estimated_time_seconds': 120,
            'check_status_url': f'/api/generate/status/{generation_id}'
        }), 202
    
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500


def _process_generation(generation_id, input_file, language, n_samples, reference_char_ids):
    """
    Background process for font generation.
    This is a stub that simulates the DeepVecFont-v2 pipeline.
    """
    try:
        task = generation_tasks[generation_id]
        task['status'] = 'processing'
        task['progress'] = 10
        
        # TODO: Integrate actual DeepVecFont-v2 model
        # 1. Load input file (TTF or image)
        # 2. Preprocess based on language
        # 3. Run model inference
        # 4. Generate multiple candidates
        # 5. Select best using IOU
        
        results_folder = os.path.join(current_app.config['RESULTS_FOLDER'], 'fonts', generation_id)
        os.makedirs(results_folder, exist_ok=True)
        
        # Simulate progress
        task['progress'] = 50
        task['progress'] = 90
        
        # Store results metadata
        task['results'] = {
            'generation_id': generation_id,
            'language': language,
            'n_samples': n_samples,
            'output_folder': results_folder,
            'files': []
        }
        
        task['status'] = 'completed'
        task['progress'] = 100
        task['completed_at'] = datetime.now().isoformat()
        
        logger.info(f"Generation completed: {generation_id}")
    
    except Exception as e:
        logger.error(f"Generation processing error: {str(e)}")
        generation_tasks[generation_id]['status'] = 'failed'
        generation_tasks[generation_id]['error'] = str(e)


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
                'progress': task['progress']
            })
        
        return jsonify({
            'total': len(tasks),
            'tasks': tasks
        }), 200
    
    except Exception as e:
        logger.error(f"List error: {str(e)}")
        return jsonify({'error': str(e)}), 500
