# Save this as app.py

import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

# Adding a slider widget
x = st.slider("Select a value for x", 0, 100)
st.write("You selected:", x)

# Generating a sample dataframe
df = pd.DataFrame({
    'column1': np.random.randn(50),
    'column2': np.random.randn(50)
})

st.line_chart(df)
