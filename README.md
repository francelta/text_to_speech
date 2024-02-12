# text_to_speech

Document Reader and Text-to-Speech Converter


This Python script is an interactive tool that captures text from documents through a webcam, recognizes the text using Optical Character Recognition (OCR) technology, and converts the recognized text into speech. It leverages EasyOCR for text recognition, OpenCV for image processing and capturing video stream, pytesseract as an alternative OCR option, and gTTS (Google Text-to-Speech) for converting text to speech.

Features:
  Real-time text recognition from a video stream using EasyOCR.
  Alternative text recognition using pytesseract.
  Conversion of recognized text into speech using gTTS.
  Display of the video stream and identified text regions on the screen.
  Saving of recognized text into a text file for further use.

  
Prerequisites:

  Before you begin, ensure you have the following installed:

    Python 3.x
    OpenCV (cv2)
    EasyOCR
    pytesseract (optional, if you want to use Tesseract OCR as an alternative)
    gTTS for text-to-speech conversion
    playsound for playing the generated speech
    You can install the required libraries using pip:

      pip install opencv-python easyocr pytesseract gTTS playsound
      
  Note: For pytesseract, you may also need to install Tesseract OCR separately on your system.

Setup:

  Clone the repository or download the script to your local machine.
  Ensure all required libraries are installed as mentioned in the Prerequisites section.
  If using pytesseract, ensure Tesseract OCR is correctly installed and configured on your system.
  
Running the Application:

  To run the script, navigate to the script's directory in your terminal and execute:

    python document_reader_to_speech.py

Usage:

  Upon launching the application:
  
  Position a document within the designated area in the webcam's field of view.
  The script will capture the text from the document and display the recognized text on the screen.
  The recognized text is then converted into speech and played back.
  The text is also saved into a file named Info.txt for further use.
Code Explanation
OCR with EasyOCR and pytesseract: Utilizes EasyOCR for primary text recognition and pytesseract as an optional alternative.
Image Processing with OpenCV: Captures video stream, processes images, and displays the text location on the document.
Text-to-Speech: Converts recognized text into speech using gTTS and plays it using playsound.
File Operations: Saves recognized text into a file for documentation or further processing.
