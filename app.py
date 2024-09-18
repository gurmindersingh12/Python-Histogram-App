import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Scientific Histogram Generator")

# File upload
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
        ax.hist(data[column], bins=30)

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Save the plot as a TIFF image
        fig.savefig("histogram.tiff", format='tiff', dpi=300)

        # Provide a download link for the TIFF image
        with open("histogram.tiff", "rb") as file:
            btn = st.download_button(
                label="Download Histogram as TIFF",
                data=file,
                file_name="histogram.tiff",
                mime="image/tiff"
            )
