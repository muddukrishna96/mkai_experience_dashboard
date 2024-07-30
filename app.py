# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:06:57 2024

@author: muddu krishna
"""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
#------------------Set current working directory to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#------------------Function to resize image
def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

#------------------Function to rotate image
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

#------------------Function to convert image to grayscale
def grayscale_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#------------------Function to apply a blur effect
def blur_image(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


sample_images = [
    r"sample images\T1_0046_S8_png_jpg.rf.40468bf3ddc313a31a453d431e7adfe2.jpg",
    r"sample images\T1_0148_S8_png_jpg.rf.83b573f631fe81a094a74b22506b99ef.jpg",
    r"sample images\T1_0249_S8_png_jpg.rf.f19f268a8de590ac325ecc499e55fe70.jpg",
    r"sample images\T1_0311_S8_png_jpg.rf.0144375d7747c7f9db09a1c238e9a815.jpg",
    r"sample images\T1_0348_S8_png_jpg.rf.644408815cf93e14cd25d568aaf93a69.jpg"
    ]

def main():
    st.title("Image and Video Processing Application")

    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Medical Field", "Page 2"])

    if app_mode == "Medical Field":
        st.header("Upload an Image or Video")

        uploaded_file = st.file_uploader("Choose an image or video file", type=["jpg", "jpeg", "png", "mp4"])

        if uploaded_file is not None:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            if uploaded_file.type.startswith('image'):
                image = cv2.imdecode(file_bytes, 1)
            elif uploaded_file.type == "video/mp4":
                st.video(uploaded_file)
                return
        else:
            st.subheader("Or choose a sample image")
            selected_sample = st.selectbox("Select a sample image", sample_images)
            if selected_sample:
                image = cv2.imread(selected_sample)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if 'image' in locals():
            st.image(image, caption='Uploaded Image', use_column_width=True)

            st.subheader("Choose an operation")
            operation = st.radio("Select an operation", ["Resize", "Rotate", "Grayscale", "Blur"])

            if operation == "Resize":
                width = st.slider("Width", 50, 800, image.shape[1])
                height = st.slider("Height", 50, 800, image.shape[0])
                if st.button("Apply"):
                    processed_image = resize_image(image, width, height)
                    st.image(processed_image, caption='Processed Image', use_column_width=True)

            elif operation == "Rotate":
                angle = st.slider("Angle", -180, 180, 0)
                if st.button("Apply"):
                    processed_image = rotate_image(image, angle)
                    st.image(processed_image, caption='Processed Image', use_column_width=True)

            elif operation == "Grayscale":
                if st.button("Apply"):
                    processed_image = grayscale_image(image)
                    st.image(processed_image, caption='Processed Image', use_column_width=True)

            elif operation == "Blur":
                kernel_size = st.slider("Kernel Size", 1, 20, 5, step=2)
                if st.button("Apply"):
                    processed_image = blur_image(image, kernel_size)
                    st.image(processed_image, caption='Processed Image', use_column_width=True)

    elif app_mode == "Page 2":
        st.header("Page 2")
        st.subheader("Under Construction")

if __name__ == "__main__":
    main()
