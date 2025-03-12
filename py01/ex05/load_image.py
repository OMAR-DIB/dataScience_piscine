from matplotlib import pyplot as plt
import numpy as np
import PIL.Image


def ft_load(path: str) -> np.ndarray:
    try:
        img = PIL.Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            return ValueError("Unsupported image format.\
                Only JPG and JPEG are allowed.")

        # print("Image format:", img.format)
        width, height = img.size
        # print(f"Image size: {width}x{height} pixels")

        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        # print("Pixel content in RGB format:")
        print(img_array)
        plt.imshow(img_array)
        plt.axis('off')
        plt.title("Original Image")
        plt.show()

        return img_array
    except ValueError as e:
        print(f"Error: {e}")


# def zoom_image(img_array: np.ndarray, zoom_factor: float) -> np.ndarray:
#     # Calculate the center of the image
#     height, width = img_array.shape[:2]
#     center_x, center_y = width // 2, height // 2

#     # Calculate the new dimensions after zooming
#     new_width = int(width / zoom_factor)
#     new_height = int(height / zoom_factor)

#     # Slice the image to zoom
#     zoomed_array = img_array[
#         center_y - new_height // 2: center_y + new_height // 2,
#         center_x - new_width // 2: center_x + new_width // 2,
#     ]

#     print("New shape after slicing:", zoomed_array.shape)
#     print(zoomed_array)

#     return zoomed_array

# def display_image(zoomed_array: np.ndarray, title: str):
#     plt.imshow(zoomed_array)
#     plt.title(title)
#     plt.axis('on')  # Show scale on x and y axis
#     plt.show()

# if __name__ == "__main__":
#     # Load the image
#     img_array = ft_load("../images/animal.jpeg")

#     if img_array is not None:
#         zoomed_array = zoom_image(img_array, zoom_factor=2.5)

#         # Display the zoomed image
#         display_image(zoomed_array, "Zoomed Image")
