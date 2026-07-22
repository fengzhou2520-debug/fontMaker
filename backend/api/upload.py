"""
File upload handling for fonts and images.
"""

import os
import uuid
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

upload_bp = Blueprint('upload', __name__, url_prefix='/api')


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    Upload font file or image sample.
    
    Request:
    - file: .ttf/.otf or image file (required)
    - language: target language code (required)
    - description: description of the sample (optional)
    
    Response:
    - task_id: unique task identifier
    - file_path: uploaded file path
    - language: target language
    - timestamp: upload timestamp
    """
    try:
        # Validate request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        if 'language' not in request.form:
            return jsonify({'error': 'No language specified'}), 400
        
        file = request.files['file']
        language = request.form.get('language')
        description = request.form.get('description', '')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Supported: ttf, otf, png, jpg, jpeg, gif, bmp'}), 400
        
        # Create unique task ID and filename
        task_id = str(uuid.uuid4())
        file_ext = secure_filename(file.filename).rsplit('.', 1)[1].lower()
        unique_filename = f"{task_id}.{file_ext}"
        
        # Save file
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, unique_filename)
        file.save(file_path)
        
        logger.info(f"File uploaded: {task_id} for language {language}")
        
        return jsonify({
            'success': True,
            'task_id': task_id,
            'file_path': f'/uploads/{unique_filename}',
            'language': language,
            'description': description,
            'file_size': os.path.getsize(file_path),
            'timestamp': datetime.now().isoformat(),
            'status': 'uploaded'
        }), 200
    
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': f'Upload failed: {str(e)}'}), 500


@upload_bp.route('/upload/status/<task_id>', methods=['GET'])
def upload_status(task_id):
    """
    Check the status of an uploaded file.
    """
    try:
        upload_folder = current_app.config['UPLOAD_FOLDER']
        # Find file with task_id
        for filename in os.listdir(upload_folder):
            if filename.startswith(task_id):
                file_path = os.path.join(upload_folder, filename)
                return jsonify({
                    'task_id': task_id,
                    'status': 'exists',
                    'file_size': os.path.getsize(file_path),
                    'created_at': datetime.fromtimestamp(os.path.getctime(file_path)).isoformat()
                }), 200
        
        return jsonify({'error': f'Task {task_id} not found'}), 404
    
    except Exception as e:
        logger.error(f"Status check error: {str(e)}")
        return jsonify({'error': str(e)}), 500
