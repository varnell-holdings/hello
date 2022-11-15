import streamlit as st

st.title('BMI Calculator')

weight = st.slider('Choose weight - kg', 20, 200, value=75)

weight

height = st.slider('Choose height - cm', 100, 240, value=170)

height

height_meters = height / 100

bmi = weight / (height_meters ** 2)

st.write('BMI is')

bmi

