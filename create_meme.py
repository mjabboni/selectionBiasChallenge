"""
Create Final Statistics Meme

This module assembles all four panels into a professional-looking
four-panel meme demonstrating selection bias.
"""

import numpy as np
import matplotlib.pyplot as plt


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Create a four-panel statistics meme demonstrating selection bias.
    
    The meme shows:
    1. Reality - The original image (true population)
    2. Your Model - The stippled image (data collection/sampling)
    3. Selection Bias - The block letter showing systematic missing pattern
    4. Biased Estimate - The masked stippled image (biased estimate)
    
    Parameters
    ----------
    original_img : np.ndarray
        The original grayscale image
    stipple_img : np.ndarray
        The stippled version of the image
    block_letter_img : np.ndarray
        The block letter mask image
    masked_stipple_img : np.ndarray
        The stippled image with mask applied
    output_path : str
        Path where the meme PNG will be saved
    dpi : int, optional
        Resolution in dots per inch (default is 150)
        Higher values (200-300) give better quality
    background_color : str, optional
        Background color for the figure (default is "white")
        Can be any matplotlib color name or hex code
    
    Returns
    -------
    None
        Saves the meme to the specified output path
    """
    # Create figure with 2x2 subplots matching the QMD layout
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), facecolor=background_color)
    
    # Original Image (Reality) - Top Left
    axes[0, 0].imshow(original_img, cmap='gray')
    axes[0, 0].set_title('Reality', fontsize=18, fontweight='bold')
    axes[0, 0].axis('off')
    
    # Stippled Image (Your Model) - Top Right
    axes[0, 1].imshow(stipple_img, cmap='gray')
    axes[0, 1].set_title('Your Model', fontsize=18, fontweight='bold')
    axes[0, 1].axis('off')
    
    # Block Letter (Selection Bias Pattern) - Bottom Left
    axes[1, 0].imshow(block_letter_img, cmap='gray')
    axes[1, 0].set_title('Selection\n Bias (S)', fontsize=18, fontweight='bold')
    axes[1, 0].axis('off')
    
    # Masked Stipple (Biased Estimate) - Bottom Right
    axes[1, 1].imshow(masked_stipple_img, cmap='gray')
    axes[1, 1].set_title('Biased\n Estimate', fontsize=18, fontweight='bold')
    axes[1, 1].axis('off')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(
        output_path,
        dpi=dpi,
        bbox_inches='tight',
        facecolor=background_color,
        edgecolor='none'
    )
    
    # Close the figure to free memory
    plt.close(fig)
    
    print(f"✅ Meme saved successfully to: {output_path}")

