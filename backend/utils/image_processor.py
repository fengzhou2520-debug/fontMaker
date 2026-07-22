"""
Utility functions for image and font processing.
"""

import cv2
import numpy as np
from PIL import Image
import os
from pathlib import Path


def load_image(image_path, size=(256, 256)):
    """
    Load and preprocess image for font generation.
    
    Args:
        image_path: Path to image file
        size: Target image size (height, width)
    
    Returns:
        numpy array of preprocessed image
    """
    try:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        # Resize to target size
        img_resized = cv2.resize(img, size)
        
        # Normalize to [0, 1]
        img_normalized = img_resized.astype(np.float32) / 255.0
        
        return img_normalized
    
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def preprocess_font_sample(file_path, language='en'):
    """
    Preprocess font or image sample for model input.
    
    Args:
        file_path: Path to TTF/OTF/image file
        language: Target language code
    
    Returns:
        Preprocessed tensor ready for model
    """
    try:
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext in ['.ttf', '.otf']:
            # Extract glyphs from font file
            return extract_glyphs(file_path, language)
        elif ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            # Load and preprocess image
            return load_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    
    except Exception as e:
        print(f"Preprocessing error: {e}")
        return None


def extract_glyphs(font_path, language='en', char_indices=None):
    """
    Extract glyph images from font file.
    
    Args:
        font_path: Path to TTF/OTF font file
        language: Language code
        char_indices: Specific character indices to extract
    
    Returns:
        Dictionary of glyph images
    """
    # TODO: Implement glyph extraction using fontTools or FontForge
    glyphs = {}
    return glyphs


def validate_image(image_path, min_size=(32, 32), max_size=(2048, 2048)):
    """
    Validate image file before processing.
    
    Args:
        image_path: Path to image file
        min_size: Minimum allowed dimensions
        max_size: Maximum allowed dimensions
    
    Returns:
        Boolean indicating if image is valid
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Check dimensions
        if width < min_size[0] or height < min_size[1]:
            print(f"Image too small: {width}x{height}")
            return False
        
        if width > max_size[0] or height > max_size[1]:
            print(f"Image too large: {width}x{height}")
            return False
        
        return True
    
    except Exception as e:
        print(f"Image validation error: {e}")
        return False


def validate_font(font_path):
    """
    Validate font file before processing.
    
    Args:
        font_path: Path to TTF/OTF font file
    
    Returns:
        Boolean indicating if font is valid
    """
    try:
        # TODO: Implement font validation using fontTools
        return True
    except Exception as e:
        print(f"Font validation error: {e}")
        return False
