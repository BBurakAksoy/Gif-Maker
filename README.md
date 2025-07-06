GIF Creator

This Python script converts a set of images from a specified folder into an animated GIF.

Features

Supports .png, .jpg, and .jpeg formats

Resizes all images to a standard size of 800x600 pixels

Creates a GIF with 0.4s frame duration

Loops the animation infinitely

Requirements

Ensure you have the following dependencies installed:

pip install numpy pillow imageio

Usage

Run the script:

python script.py

Enter the folder path containing the images when prompted.

The output GIF will be saved as new_gif.gif.

Notes

The images are sorted alphabetically before creating the GIF.

If no valid images are found, the script will display an error message.


