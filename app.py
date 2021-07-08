import streamlit as st
import pytesseract
import numpy as np
from PIL import Image

st.title('OPTICAL CHARACTER RECOGNIZER')
st.write('Using Tesseract')
st.text_input("Done by SHEKHAR")
# st.write("My name is ",a)
upload = st.file_uploader("Choose an Image")
if upload is not None:
  img = Image.open(upload)
  st.image(img,caption = 'UPLOADED IMAGE',use_column_width=True)

  if st.button('PREDICT'):
    st.write("RESULT....")
    extract = pytesseract.image_to_string(img)
    st.title(extract)