# Import required libraries
# streamlit: For creating web applications
import streamlit as st
# numpy: For handling numerical operations and image data
import numpy as np
# pytesseract: Python wrapper for Tesseract, used for Optical Character Recognition (OCR)
import pytesseract
# PIL (Python Imaging Library): For opening and manipulating images
from PIL import Image
# cv2 (OpenCV): For advanced image processing
import cv2

# Configure Pytesseract to point to the Tesseract executable
# This path should be updated based on where Tesseract is installed on your machine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the web app displayed in the Streamlit interface
st.title("Handwritten English Text Recognition")

st.write("Please upload an image of handwritten English text, and the model will extract the text.")


# Function to preprocess the uploaded image for OCR
def preprocess_image(image):
    """
    Preprocess the uploaded image for OCR by converting it to grayscale, 
    applying Gaussian blur, and then thresholding the image.
    
    Args:
        image (PIL.Image): Input image uploaded by the user.
        
    Returns:
        dilated_image (ndarray): Preprocessed image ready for OCR.
    """
    # Convert the image to grayscale for better OCR performance
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur to smooth the image and reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply thresholding to convert the image into a binary (black and white) image
    # This helps to enhance the text for better recognition
    _, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

    # Optional: Dilate the image to thicken the text lines, making them easier to recognize
    kernel = np.ones((3, 3), np.uint8)  # Define a kernel for dilation
    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

    return dilated_image

# Function to perform OCR (Optical Character Recognition) using Pytesseract
def perform_ocr(image):
    """
    Perform OCR on the preprocessed image using Pytesseract.
    
    Args:
        image (ndarray): Preprocessed image ready for OCR.
        
    Returns:
        text (str): Extracted text from the image.
    """
    # Custom configuration for Pytesseract
    # --oem 1 specifies using the LSTM OCR engine (neural network-based)
    # --psm 6 sets the page segmentation mode to assume a single uniform block of text
    custom_config = r'--oem 1 --psm 6'

    # Perform OCR using Pytesseract, specifying English language
    text = pytesseract.image_to_string(image, lang='eng', config=custom_config)
    
    # Return the extracted text after stripping any extra whitespaces
    return text.strip()

# Streamlit file uploader component: Allows the user to upload an image file
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp", "tiff"])

# If an image is uploaded, process it
if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)

    # Display the uploaded image on the Streamlit app
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Placeholder text that displays "Processing..." while the OCR is being performed
    processing_placeholder = st.empty()
    processing_placeholder.text("Processing...")

    # Preprocess the image to prepare it for OCR
    processed_image = preprocess_image(image)

    # Perform OCR to extract text from the preprocessed image
    extracted_text = perform_ocr(processed_image)

    # Remove the "Processing..." message after OCR is done
    processing_placeholder.empty()

    # Display the extracted text in the app
    st.write("Extracted Text:")
    st.write(extracted_text)

