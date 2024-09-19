import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Scientific Data Visualization Tool")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())

    # Column selection
    column = st.selectbox("Select column for plotting", data.columns)

    # Plot type selection (Histogram or Bar Chart)
    plot_type = st.selectbox("Select plot type", options=["Histogram", "Bar Chart"])

    if plot_type == "Histogram":
        # User input for bin size if Histogram is selected
        bins = st.slider("Select number of bins", min_value=5, max_value=100, value=30)
    else:
        # Custom range selection for Bar Chart
        min_value = st.number_input("Minimum value", value=float(data[column].min()))
        max_value = st.number_input("Maximum value", value=float(data[column].max()))

        # Number of categories (classes)
        num_categories = st.slider("Select number of categories", min_value=2, max_value=20, value=5)

    # Custom axis labels and title
    x_label = st.text_input("X-axis label", value="Values")
    y_label = st.text_input("Y-axis label", value="Frequency" if plot_type == "Histogram" else "Count")
    title = st.text_input("Plot title", value="Histogram" if plot_type == "Histogram" else "Bar Chart")

    # Font size selection
    font_size = st.slider("Font size", min_value=8, max_value=24, value=12)

    # Option to use horizontal or vertical orientation (for Histogram)
    if plot_type == "Histogram":
        orientation = st.selectbox("Select histogram orientation", options=["vertical", "horizontal"])

    # Generate plot
    if st.button("Generate Plot"):
        fig, ax = plt.subplots()

        if plot_type == "Histogram":
            ax.hist(data[column], bins=bins, orientation=orientation)
        elif plot_type == "Bar Chart":
            # Define the range of values
            bins = np.linspace(min_value, max_value, num_categories + 1)

            # Group data into categories based on the range
            categories = pd.cut(data[column], bins=bins, include_lowest=True)

            # Count occurrences in each category
            category_counts = categories.value_counts(sort=False)

            # Generate bar chart with categories
            ax.bar(category_counts.index.astype(str), category_counts.values)

        # Customize labels, title, and font sizes
        ax.set_xlabel(x_label, fontsize=font_size)
        ax.set_ylabel(y_label, fontsize=font_size)
        ax.set_title(title, fontsize=font_size)

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Save the plot as a TIFF image
        fig.savefig(f"{plot_type.lower()}_plot.tiff", format='tiff', dpi=300)

        # Provide a download link for the TIFF image
        with open(f"{plot_type.lower()}_plot.tiff", "rb") as file:
            btn = st.download_button(
                label=f"Download {plot_type} as TIFF",
                data=file,
                file_name=f"{plot_type.lower()}_plot.tiff",
                mime="image/tiff"
            )
