import os
import numpy as np
from PIL import Image
import imageio.v2 as imageio

# Folder containing images
image_folder = input("Enter the folder containing the images: ")

# Output GIF file
output_gif = "new_gif.gif"

# Standard size for all images
standard_size = (800, 600)

# Load images and convert to numpy array
images = []
for filename in sorted(os.listdir(image_folder)):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(image_folder, filename)
        img = Image.open(img_path).resize(standard_size)
        images.append(np.array(img))  # PIL Image -> Numpy Array

# Error checking
if not images:
    print(f"Error: No images found in the folder '{image_folder}'!")
else:
    # Create GIF
    imageio.mimsave(
        output_gif,
        images,
        duration=400,  # Duration in milliseconds (0.4 seconds)
        loop=0
    )
    print(f"GIF created successfully: {output_gif}")
