"""
Models package initialization with DeepVecFont-v2 setup.
"""

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

# Initialize models directory
MODELS_DIR = Path(__file__).parent
CHECKPOINTS_DIR = MODELS_DIR / 'checkpoints'
CHECKPOINTS_DIR.mkdir(exist_ok=True)

logger.info(f"Models directory: {MODELS_DIR}")
logger.info(f"Checkpoints directory: {CHECKPOINTS_DIR}")

# Import model classes
try:
    from .deepvecfont_v2 import DeepVecFontV2Model, get_model, generate_fonts_task
    logger.info("✓ DeepVecFont-v2 model imported successfully")
except ImportError as e:
    logger.warning(f"Could not import DeepVecFont-v2: {e}")

__all__ = [
    'DeepVecFontV2Model',
    'get_model',
    'generate_fonts_task',
    'MODELS_DIR',
    'CHECKPOINTS_DIR',
]
