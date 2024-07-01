import streamlit as st

from PIL import Image
import numpy as np

from utils import process_image, annotate_image

# App title
st.title("Object Detection for Images")

# Upload file
file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file is not None:
    st.image(file, caption="Uploaded Image")

    # Process and annotate image
    image = Image.open(file)
    image = np.array(image)
    detections = process_image(image)
    processed_image = annotate_image(image, detections)
    st.image(processed_image, caption="Processed Image")
