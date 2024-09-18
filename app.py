import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Title
st.title("Scientific Histogram Generator with Customization")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())

    # Column selection
    column = st.selectbox("Select column for histogram", data.columns)

    # Checkboxes for mean and median lines
    add_mean = st.checkbox("Overlay Mean")
    add_median = st.checkbox("Overlay Median")

    # User input for bin size
    bins = st.slider("Select number of bins", min_value=5, max_value=100, value=30)

    # Color palette options
    color = st.selectbox("Select color for the histogram", options=['blue','green','red','orange'])

    # Generate histogram
    if st.button("Generate Histogram"):
        fig, ax = plt.subplots()
        ax.hist(data[column], bins=bins, color=color)

        # Overlay mean and meadian if selected
        if add_mean:
            mean_value = np.mean(data[column])
            ax.axvline(mean_value, color='k', linestyle='dashed', linewidth=1)
            st.write(f"Mean: {mean_value}")
        
        if add_median:
            median_value = np.median(data[column])
            ax.axvline(median_value, color='r', linestyle='dashed', linewidth=1)
            st.write(f"Median: {median_value}")
        
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
