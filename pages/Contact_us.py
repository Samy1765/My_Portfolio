import streamlit as st
from send_emails import send_email
st.header("Contact Me")

with st.form(key="form"):
   email = st.text_input("Email Address")
   message = st.text_area("Message")
   message=f"""
Subject: New Email From {email}

From:{email}
{message}
"""
   button=st.form_submit_button("Submit")
   if button:
      send_email(message)
      st.info("Your Email Was Sent Successfully! ")