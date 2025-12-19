import streamlit as st
import joblib

model=joblib.load("spam_clf.pkl")

text=st.text_input("Enter MSG")
if st.button("Predict"):
    result=model.predict([text])
    if result=="spam":
        st.error("Spam->Irrelevent")
    else:
        st.success("Ham->Relevent")   