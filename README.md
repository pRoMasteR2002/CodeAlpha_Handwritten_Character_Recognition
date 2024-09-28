
# **Handwritten English Text Recognition**

## **Overview**

The **Handwritten English Text Recognition** project is a web application that utilizes **Optical Character Recognition (OCR)** to recognize and extract handwritten text from uploaded images. This system employs **Pytesseract**, OpenCV for image preprocessing, and **Streamlit** for creating a user-friendly web interface. Simply upload an image containing handwritten English text, and the application will extract and display the text in real time.

---

## **🌟 Project Goals**

- **Handwritten Text Recognition**: Convert handwritten text from images into digital text using OCR techniques.
- **Interactive Web Interface**: Provide an intuitive interface that allows users to upload images and retrieve extracted text in real time.
- **Advanced Image Processing**: Use OpenCV to preprocess images (grayscale conversion, blurring, thresholding, and dilation) to improve text recognition accuracy.

---

## **📈 Key Features**

- **File Upload**: Users can upload images in various formats (PNG, JPG, JPEG, BMP, TIFF).
- **Real-Time OCR Processing**: Automatically processes and extracts text from the uploaded images.
- **Image Preprocessing**: Enhances text readability by converting the image to grayscale, applying Gaussian blur, and thresholding.
- **OCR with Pytesseract**: Utilizes the Tesseract engine (LSTM-based model) to recognize English text.
- **Clean and Simple Interface**: Powered by **Streamlit**, the app offers an easy-to-use platform for image uploads and results display.

---

## **🔧 How to Use**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/pRoMasteR2002/Handwritten_English_Text_Recognition.git
cd Handwritten_English_Text_Recognition
```

### **Step 2: Set Up a Python Virtual Environment**

Creating a virtual environment ensures that all required packages and dependencies are installed in an isolated environment, preventing conflicts with system-wide packages.

1. **Create a virtual environment**:
   ```bash
   python -m venv myvenv
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     myvenv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source myvenv/bin/activate
     ```

3. **Install Dependencies**:
   Once the environment is activated, install the necessary libraries:
   ```bash
   pip install streamlit numpy pillow opencv-python
   ```

### **Step 3: Install Pytesseract**

**Pytesseract** is a Python wrapper for Google's Tesseract-OCR Engine. Follow these steps to install Pytesseract:

1. **Install Tesseract OCR**:
   - Download the Tesseract installer for Windows from [this link](https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe).
   - Run the installer and follow the prompts to install Tesseract.

2. **Add Tesseract to System Path** (if not automatically added):
   - After installation, add the Tesseract installation path to your system's PATH environment variable.
   - The default installation path is typically:
     ```
     C:\Program Files\Tesseract-OCR\
     ```
   - Follow these steps to add it to the PATH:
     - Right-click on "This PC" or "My Computer" and select "Properties."
     - Click on "Advanced system settings."
     - Click on "Environment Variables."
     - Under "System variables," find the `Path` variable and click "Edit."
     - Click "New" and add the path to the Tesseract installation.
     - Click "OK" to close all dialog boxes.

3. **Install Pytesseract in your virtual environment**:
   After setting up Tesseract, install Pytesseract using pip:
   ```bash
   pip install pytesseract
   ```

4. **Configure Pytesseract in the code**:
   - In your Python code, set the path to the Tesseract executable. Example:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### **Step 4: Download the EMNIST Dataset**
To enhance the OCR capabilities, you can download the EMNIST dataset. 

1. **Download the EMNIST dataset**:
   - Click [here to download](https://biometrics.nist.gov/cs_links/EMNIST/gzip.zip).
  
2. **Extract the dataset**:
   - After downloading, extract the contents of the `gzip.zip` file into the project directory. Ensure the images are organized in a folder named `emnist`:
   ```
   Handwritten_English_Text_Recognition/
   ├── app.py
   ├── emnist/            # Directory for the EMNIST dataset files
   └── myvenv/
   ```

### **Step 5: Run the Application**
Start the **Streamlit** application by running the following command in the terminal:
```bash
python -m streamlit run app.py
```

### **Step 6: Upload Image and Extract Text**
- Open the local URL (e.g., `http://localhost:8501`) provided by Streamlit in your browser.
- Upload an image containing handwritten English text.
- The app will display the uploaded image and process it.
- The extracted text will appear below the image.

---

## **📚 Concepts Used**

- **Optical Character Recognition (OCR)**: The core of this project, OCR is performed using **Pytesseract** to convert handwritten text from images into digital text.
- **Image Preprocessing**: To improve the accuracy of OCR, the uploaded images are preprocessed with OpenCV using grayscale conversion, blurring, thresholding, and dilation techniques.
- **Streamlit**: A Python framework for creating web applications, used to build the interface for uploading images and displaying the OCR results.

---

## **📂 Project Structure**

```
Handwritten_English_Text_Recognition/
│
├── app.py                                # Main Python script for the OCR application
├── emnist/                                # Directory for the EMNIST dataset files
└── myvenv/                                # Python virtual environment directory
```

---

## **🔮 Future Improvements**

- **Multilingual OCR**: Extend the OCR capabilities to recognize and extract handwritten text in other languages.
- **Enhanced Image Preprocessing**: Incorporate more advanced preprocessing techniques (e.g., edge detection) to handle noisy or poorly lit images.
- **User Feedback**: Allow users to edit or correct the extracted text manually.
- **Text-to-Speech Integration**: Add a feature that converts the extracted text into speech for accessibility purposes.

---

## **📜 License**

This project is licensed under the **MIT License**. Feel free to use, modify, and contribute to this project.

---

## **⚙️ Acknowledgments**

Special thanks to:
- **Pytesseract** for providing powerful OCR functionality.
- **Streamlit** for creating a simple and interactive web development platform.
- **Tesseract OCR** engine for enabling accurate text recognition.
