import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Simple Histogram Generator")

# Basic Instruction
st.write("Upload your CSV file to generate a histogram")

# File Upload

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())

    # Column selection
    column = st.selectbox("Select column for histogram", data.columns)

    # Generate histogram
    if st.button("Generate Histogram"):
        fig, ax = plt.subplots()
        ax.hist(data[column],  bins=30)
        st.pyplot(fig)
        