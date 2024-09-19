import streamlit as st

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
   image=st.image("images for my portfolio/my_img.png",width=400)

with col2:
   st.title("Swayam Deshmukh")
   content="""
Hello! I'm Swayam Deshmukh

Welcome to my corner of the web! I'm a Student in JSPM's RSCOE.

Through my work, I aim to combine creativity with strategy, offering solutions that are both innovative and effective. Whether it's [mention specific services or products you offer], my focus is always on delivering high-quality results that make an impact.

When I'm not Coding, you can find me Watching Animes, Reading Books.

Feel free to explore my work, and don’t hesitate to get in touch if you'd like to collaborate or learn more!
"""
   st.write(content)

