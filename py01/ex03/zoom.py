import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def trim(array : np.array, x : int, y : int, width : int, height : int, depth=3) -> np.array :
    """
        Trim an array using the given parameters
    """
    return array[y:y+width, x:x+height, :depth]


def main():
    """
        Open the image, trim it and convert it to grayscale,
        then display it.
    """

    try:
        image = ft_load('../images/animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    print('The shape of image is', image.shape)
    print(image)

    image = trim(image, 450, 100, 400, 400, 1)

    print(f'New shape after slicing: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    # Display the image
    # image = np.squeeze(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
