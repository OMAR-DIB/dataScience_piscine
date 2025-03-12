import PIL.Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = PIL.Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Unsupported image format.\
                Only JPG and JPEG are allowed.")

        # print("Image format:", img.format)

        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        # print("Pixel content in RGB format:")
        print(img_array)

        return img_array
    except ValueError as e:
        print(f"Error: {e}")


# image_array = ft_load("../images/landscape.jpg")
