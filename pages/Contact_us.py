import streamlit as st
from send_emails import send_email
st.header("Contact Me")

with st.form(key="form"):
   email = st.text_input("Email Address")
   message = st.text_area("Message")
   button=st.form_submit_button("Submit")
   st.send_email(message)