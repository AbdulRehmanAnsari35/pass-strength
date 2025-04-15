import streamlit as st
import re

st.set_page_config(page_title="password strength checker",page_icon="🔒")

st.title("🔒password strength checker")
st.markdown("""
## Welcome to the ultimate password strength checker!👌 
use this simple tool to check the strngth of your password and get suggestions on how to make it stronger
            we will give you to helpfull tips to create a **strong password** 🔒""" )

password = st.text_input("Enter your password", type= "password")

feedback = []

score = 0
 
if password:
    if len("password") >= 8:
        score += 1
    else:
        feedback.append("❌password should be 8 characters long.")
        
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
       score += 1
    else:
        feedback.append("❌password should contain upper and lower characters.") 
    if re.search(r'\d', password):  
        score += 1
    else:
        feedback.append("❌password should contain at least one digit.")
    if re.search('[!@#$%&*]',password):  
        score += 1
    else:
        feedback.append("❌password should contain at least one special characters(!@#$%&*).") 
    if score == 4:
        feedbackback.append("✅Your password is strong!🍧")
    elif score == 3:
        feedback.append("🟡Your password is medium strength. it could be stronger.")  
    else:
        feedback.append("🟠Your password is too week.Please make it stronger") 

    if feedback:
        st.markdown("## Improvement suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")

