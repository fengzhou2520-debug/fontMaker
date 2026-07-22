#!/usr/bin/env python
"""
Flask application for multilingual font generation using DeepVecFont-v2.
"""

import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging
from datetime import datetime

from api.upload import upload_bp
from api.generate import generate_bp
from api.download import download_bp
from writing_systems import WRITING_SYSTEMS_MAP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Flask app setup
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['RESULTS_FOLDER'] = os.path.join(os.getcwd(), 'results')
app.config['ALLOWED_EXTENSIONS'] = {'ttf', 'otf', 'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(app.config['RESULTS_FOLDER'], 'fonts'), exist_ok=True)

# CORS setup
CORS(app)

# Register blueprints
app.register_blueprint(upload_bp)
app.register_blueprint(generate_bp)
app.register_blueprint(download_bp)


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200


@app.route('/api/writing-systems', methods=['GET'])
def get_writing_systems():
    """
    Get list of all supported writing systems.
    Returns 150+ writing systems with metadata.
    """
    return jsonify({
        'total': len(WRITING_SYSTEMS_MAP),
        'systems': WRITING_SYSTEMS_MAP
    }), 200


@app.route('/api/writing-systems/<language_code>', methods=['GET'])
def get_writing_system_details(language_code):
    """
    Get details for a specific writing system.
    """
    system = WRITING_SYSTEMS_MAP.get(language_code)
    if not system:
        return jsonify({'error': f'Writing system {language_code} not found'}), 404
    
    return jsonify(system), 200


@app.route('/api/info', methods=['GET'])
def get_app_info():
    """
    Get application information and capabilities.
    """
    return jsonify({
        'name': 'Multilingual Font Maker',
        'version': '1.0.0',
        'description': 'Create fonts for 150+ writing systems using DeepVecFont-v2',
        'baseUrl': request.base_url,
        'maxUploadSize': '500MB',
        'supportedFormats': {
            'fonts': ['ttf', 'otf'],
            'images': ['png', 'jpg', 'jpeg', 'gif', 'bmp']
        },
        'writingSystemsCount': len(WRITING_SYSTEMS_MAP),
        'features': [
            'Font conversion across languages',
            'Custom font generation from samples',
            'Few-shot learning with minimal examples',
            'Batch character generation',
            'IOU-based quality selection',
            'SVG vector font output'
        ]
    }), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal server error: {error}')
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=debug_mode
    )
