# Question 5 and 6

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def hide_image():
    cover_path = filedialog.askopenfilename()
    secret_path = filedialog.askopenfilename()

    cover_image = cv2.imread(cover_path)
    secret_image = cv2.imread(secret_path)

    secret_resized = cv2.resize(secret_image, (cover_image.shape[1], cover_image.shape[0]))

    stego_image = (cover_image & 0b11111100) | (secret_resized >> 6)

    cv2.imwrite("stego_output.png", stego_image)
    print("Image hidden successfully!")

def extract_image():
    stego_path = filedialog.askopenfilename()
    stego_image = cv2.imread(stego_path)

    extracted_image = (stego_image & 0b00000011) << 6
    cv2.imwrite("extracted_output.png", extracted_image)
    print("Image extracted successfully!")

# GUI
root = tk.Tk()
root.title("Image Steganography")

tk.Button(root, text="Hide Image", command=hide_image).pack()
tk.Button(root, text="Extract Image", command=extract_image).pack()

root.mainloop()