import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


a = {'a':2, 'b':3, 'c':99}

st.header("st.button")


# if st.button("say hullo"):
#     st.write("why hello there!")
# else:
st.write("below is a dictionary.",a)

st.text('ttesting')

st.write('Hello, *World!* :sunglasses:')
st.write(1265)


df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
st.write(df2)