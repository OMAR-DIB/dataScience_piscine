import numpy as np  
from load_image import ft_load
import matplotlib.pyplot as plt

def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the colors of the image."""
    return 255 - array  # Subtract pixel values from 255

def ft_red(array: np.ndarray) -> np.ndarray:
    """Extracts the red channel."""
    red_channel = np.zeros_like(array)
    red_channel[:, :, 0] = array[:, :, 0]  # Keep only red
    return red_channel

def ft_green(array: np.ndarray) -> np.ndarray:
    """Extracts the green channel."""
    green_channel = np.zeros_like(array)
    green_channel[:, :, 1] = array[:, :, 1]  # Keep only green
    return green_channel

def ft_blue(array: np.ndarray) -> np.ndarray:
    """Extracts the blue channel."""
    blue_channel = np.zeros_like(array)
    blue_channel[:, :, 2] = array[:, :, 2]  # Keep only blue
    return blue_channel

def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    grey_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])  # Weighted grayscale conversion
    return grey_array.astype(np.uint8)

def main():
    """Loads the image, applies transformations, and displays all results in a grid."""
    image_path = '../images/landscape.jpg'  # Change this to the correct path
    image = ft_load(image_path)

    if image is None:
        return

    # Apply transformations
    transformations = [
        ("Original", image),
        ("Invert", ft_invert(image)),
        ("Red", ft_red(image)),
        ("Green", ft_green(image)),
        ("Blue", ft_blue(image)),
        ("Grey", ft_grey(image))
    ]

    # Create a 2x3 grid for displaying images
    fig, axes = plt.subplots(3, 2, figsize=(12, 8))
    for ax, (title, img) in zip(axes.flatten(), transformations):
        if len(img.shape) == 2:  # Greyscale image
            ax.imshow(img, cmap='gray')
        else:
            ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()