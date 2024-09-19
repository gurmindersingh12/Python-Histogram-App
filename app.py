import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

    # User input for bin size
    bins = st.slider("Select number of bins", min_value=5, max_value=100, value=30)

    # Custom axis labels and title
    x_label = st.text_input("X-axis label", value="Values")
    y_label = st.text_input("Y-axis label", value="Frequency")
    title = st.text_input("Plot title", value="Histogram")

    # Font size selection
    font_size = st.slider("Font size", min_value=8, max_value=24, value=12)

    # Custom bin ranges (optional)
    bin_min = st.number_input("Minimum bin value", value=float(data[column].min()))
    bin_max = st.number_input("Maximum bin value", value=float(data[column].max()))

    # Option for custom bin ranges
    custom_bins = st.checkbox("Use custom bin ranges")

    # Orientation option
    orientation = st.selectbox("Select histogram orientation", options=["vertical", "horizontal"])

    # Generate histogram
    if st.button("Generate Histogram"):
        fig, ax = plt.subplots()

        # Check if custom bin ranges should be used
        if custom_bins:
            bins = list(range(int(bin_min), int(bin_max) + 1))

        # Generate histogram with selected options
        ax.hist(data[column], bins=bins, orientation=orientation)

        # Customize labels, title, and font sizes
        ax.set_xlabel(x_label, fontsize=font_size)
        ax.set_ylabel(y_label, fontsize=font_size)
        ax.set_title(title, fontsize=font_size)

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Save the plot as a TIFF image
        fig.savefig("custom_histogram.tiff", format='tiff', dpi=300)

        # Provide a download link for the TIFF image
        with open("custom_histogram.tiff", "rb") as file:
            btn = st.download_button(
                label="Download Histogram as TIFF",
                data=file,
                file_name="custom_histogram.tiff",
                mime="image/tiff"
            )
