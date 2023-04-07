import streamlit as st
import pandas as pd
import numpy as np

st.title('Largest of three numbers')


number = st.number_input('Enter any number', 1)

number2 = st.number_input('Enter any number', 2)

number3 = st.number_input('Enter any number', 3)

if st.button('Find Largest'):
    largest = max([number, number2, number3])
    st.write('### The largest of the 3 numbers is ', largest)


st.write("# Student Details")
st.write("* Email: 21f1000560@ds.study.iitm.ac.in")
st.write("* Name: Dinesh Kumar S")
st.write("* Date: 7th Apr 2023")