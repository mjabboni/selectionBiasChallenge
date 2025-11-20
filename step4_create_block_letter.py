"""
Step 4: Create Block Letter S

This module creates a block letter "S" matching the image dimensions.
The letter represents the "selection bias" pattern in the statistics meme.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9
) -> np.ndarray:
    """
    Create a block letter matching the specified image dimensions.
    
    Parameters
    ----------
    height : int
        Height of the output image in pixels
    width : int
        Width of the output image in pixels
    letter : str, optional
        The letter to draw (default is "S")
    font_size_ratio : float, optional
        Size ratio relative to image dimensions (default is 0.9)
        
    Returns
    -------
    np.ndarray
        A 2D numpy array (height × width) with values in [0, 1]
        Black letter (0.0) on white background (1.0)
    """
    # Create a white image
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    
    # Try multiple font paths for cross-platform compatibility
    font_paths = [
        'arialbd.ttf',  # Windows
        'Arial Bold.ttf',  # macOS
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',  # Linux
        '/System/Library/Fonts/Helvetica.ttc',  # macOS alternative
        'C:\\Windows\\Fonts\\arialbd.ttf',  # Windows full path
        'C:\\Windows\\Fonts\\arial.ttf',  # Windows Arial regular
    ]
    
    # Calculate initial font size
    target_size = int(min(height, width) * font_size_ratio)
    
    font = None
    for font_path in font_paths:
        try:
            font = ImageFont.truetype(font_path, size=target_size)
            break
        except (OSError, IOError):
            continue
    
    # Fallback to default font if no TrueType font found
    if font is None:
        try:
            font = ImageFont.load_default()
            # Scale up the default font by drawing larger
            target_size = int(min(height, width) * 0.7)
        except:
            font = None
    
    # Get text bounding box to center the letter
    if font:
        # Use textbbox for better positioning
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        # Estimate if we don't have font metrics
        text_width = width // 2
        text_height = height // 2
    
    # Center the text
    x = (width - text_width) // 2 - (bbox[0] if font else 0)
    y = (height - text_height) // 2 - (bbox[1] if font else 0)
    
    # Draw the letter in black
    draw.text((x, y), letter, fill=0, font=font)
    
    # Convert to numpy array and normalize to [0, 1]
    letter_array = np.array(img, dtype=np.float64) / 255.0
    
    return letter_array

