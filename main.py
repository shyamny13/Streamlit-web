import streamlit as st
import pandas as pd
st.title("welcome to Website")
st.header("Hello Sir")
st.subheader("title")

name = st.text_input("enter ur name")
Fname  = st.text_input("enter fathers name")
Text = st.text_area("enter ur text")
options = "1","2","3","4"
classdata = st.selectbox("enter your class", options)
Done = st.button("Done")
if Done:
    st.markdown(f"""
            Name = {name}\n
            Father_Name = {Fname}\n
            Text = {Text}\n
            Class = {classdata}\n
            """)





