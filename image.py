import streamlit as st
from PIL import Image

image = Image.open(f'KABIR ARYA.png')
col1, col2 = st.columns([0.1, 0.4])
with col1:
    st.markdown("""<style> font{font-size:5px; font-family:'Cooper Black';color:#FF9633;<style><p>Result</p>""",
                unsafe_allow_html=True)
with col2:
    st.image(image, width=350)
