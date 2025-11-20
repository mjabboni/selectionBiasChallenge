"""
Step 5: Create Masked Stippled Image

This module applies the block letter mask to the stippled image,
demonstrating how selection bias removes data points in a systematic pattern.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:
    """
    Apply a mask to the stippled image by removing stipples where the mask is dark.
    
    This creates the "biased estimate" by systematically removing data points
    where the mask (selection bias) is present.
    
    Parameters
    ----------
    stipple_img : np.ndarray
        The stippled image (2D array with values in [0, 1])
        White background (1.0) with black stipples (0.0)
    mask_img : np.ndarray
        The mask image (2D array with values in [0, 1])
        Black areas (< threshold) indicate where to remove stipples
        White areas (>= threshold) indicate where to keep stipples
    threshold : float, optional
        Threshold for determining mask areas (default is 0.5)
        Pixels below this value are considered part of the mask
        
    Returns
    -------
    np.ndarray
        Masked stippled image with same shape as input
        Areas where mask is dark become white (stipples removed)
    """
    # Ensure inputs are numpy arrays
    stipple_img = np.array(stipple_img, dtype=np.float64)
    mask_img = np.array(mask_img, dtype=np.float64)
    
    # Check that dimensions match
    if stipple_img.shape != mask_img.shape:
        raise ValueError(
            f"Image dimensions must match. "
            f"Stipple: {stipple_img.shape}, Mask: {mask_img.shape}"
        )
    
    # Create output image starting with the stippled image
    masked_img = stipple_img.copy()
    
    # Where mask is dark (below threshold), remove stipples (set to white/1.0)
    # This simulates systematic missing data - the "S" pattern of selection bias
    mask_areas = mask_img < threshold
    masked_img[mask_areas] = 1.0
    
    return masked_img

