"""
Font result download and export.
"""

import os
import json
from flask import Blueprint, jsonify, current_app, send_file, send_from_directory
import logging

logger = logging.getLogger(__name__)

download_bp = Blueprint('download', __name__, url_prefix='/api')


@download_bp.route('/download/<task_id>/svg', methods=['GET'])
def download_svg(task_id):
    """
    Download generated fonts as SVG files.
    """
    try:
        results_folder = os.path.join(current_app.config['RESULTS_FOLDER'], 'fonts', task_id)
        
        if not os.path.exists(results_folder):
            return jsonify({'error': f'Results for task {task_id} not found'}), 404
        
        # Find SVG files
        svg_files = [f for f in os.listdir(results_folder) if f.endswith('.svg')]
        
        if not svg_files:
            return jsonify({'error': 'No SVG files found'}), 404
        
        # TODO: Create a zip file with all SVG results
        return jsonify({
            'task_id': task_id,
            'files': svg_files,
            'count': len(svg_files)
        }), 200
    
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@download_bp.route('/download/<task_id>/ttf', methods=['GET'])
def download_ttf(task_id):
    """
    Download generated fonts as TTF files.
    
    TODO: Implement SVG to TTF conversion
    """
    try:
        results_folder = os.path.join(current_app.config['RESULTS_FOLDER'], 'fonts', task_id)
        
        if not os.path.exists(results_folder):
            return jsonify({'error': f'Results for task {task_id} not found'}), 404
        
        return jsonify({
            'task_id': task_id,
            'message': 'TTF conversion feature coming soon',
            'status': 'not_implemented'
        }), 202
    
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@download_bp.route('/results/<task_id>', methods=['GET'])
def get_results(task_id):
    """
    Get results metadata for a completed generation task.
    """
    try:
        results_folder = os.path.join(current_app.config['RESULTS_FOLDER'], 'fonts', task_id)
        metadata_file = os.path.join(results_folder, 'metadata.json')
        
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
            return jsonify(metadata), 200
        
        if os.path.exists(results_folder):
            # List available files
            files = os.listdir(results_folder)
            return jsonify({
                'task_id': task_id,
                'files': files,
                'folder': results_folder
            }), 200
        
        return jsonify({'error': f'Results for task {task_id} not found'}), 404
    
    except Exception as e:
        logger.error(f"Results error: {str(e)}")
        return jsonify({'error': str(e)}), 500
