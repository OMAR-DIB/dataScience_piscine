import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


# def trim(array, x, y, width, height, depth=3):
#     """
#     Trim an array using the given parameters
#     """
#     return array[y:y+height, x:x+width, :depth]

def trim(array: np.array, x: int, y: int, width: int, height: int, depth=3)\
        -> np.array:
    """
        Trim an array using the given parameters
    """
    return array[y:y+width, x:x+height, :depth]


def manual_transpose(image: str):
    """
    Manually transpose a 2D image array.
    """
    # Ensure the image is 2D
    if len(image.shape) > 2:
        image = np.squeeze(image)  # Remove singleton dimensions

    rows, cols = image.shape
    transposed_image = np.zeros((cols, rows))
    # Create an empty array for the transposed image
    # print('-'*30)
    # print(image[1, 5])
    # print('-'*30)
    for i in range(rows):
        for j in range(cols):
            transposed_image[j, i] = image[i, j]  # Swap rows and columns

    return transposed_image


def main():
    """
    Open the image, trim it, convert it to grayscale, transpose it,
    and display it.
    """
    try:
        image = ft_load('../images/animal.jpeg')  # Load the image
    except Exception as e:
        print(e)
        exit()

    # print('The shape of image is', image.shape)
    # print(image)

    # Crop a square portion of the image
    image = trim(image, 450, 100, 400, 400, 1)

    print(f'The shape of image is {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    # Convert to grayscale (if not already)
    # if len(image.shape) == 3 and image.shape[2] == 3:
    #     image = np.mean(image, axis=2).astype(np.uint8) # grayscale

    # Transpose the image
    transposed_image = manual_transpose(image)
    print("New shape after Transpose:", transposed_image.shape)
    # print("Pixel content after Transpose:")
    print(transposed_image)

    # Ensure the transposed image is 2D for display
    # if len(transposed_image.shape) == 3 and transposed_image.shape[0] == 1:
    #     transposed_image = np.squeeze(transposed_image, axis=0)

    # Display the transposed image
    plt.imshow(transposed_image, cmap='gray')
    # plt.title("Transposed Image")
    plt.axis('on')  # Show axis with scale
    plt.show()


if __name__ == "__main__":
    main()
