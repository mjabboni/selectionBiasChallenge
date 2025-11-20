"""
Create Final Statistics Meme

This module assembles all four panels into a professional-looking
four-panel meme demonstrating selection bias.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


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
    4. Estimate - The masked stippled image (biased estimate)
    
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
    # Panel titles and images
    panels = [
        ("Reality", original_img),
        ("Your Model", stipple_img),
        ("Selection Bias", block_letter_img),
        ("Estimate", masked_stipple_img)
    ]
    
    # Create figure with 1×4 layout (four panels side by side)
    fig = plt.figure(figsize=(16, 4.5), facecolor=background_color)
    
    # Create grid for better layout control
    gs = GridSpec(1, 4, figure=fig, wspace=0.15, hspace=0.1)
    
    # Create each panel
    for idx, (title, img) in enumerate(panels):
        ax = fig.add_subplot(gs[0, idx])
        
        # Display the image
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        
        # Add title above each panel
        ax.set_title(
            title,
            fontsize=16,
            fontweight='bold',
            pad=15
        )
    
    # Add overall title
    fig.suptitle(
        'Statistics Meme: Selection Bias in Action',
        fontsize=20,
        fontweight='bold',
        y=0.98
    )
    
    # Adjust layout to prevent title overlap
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
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

