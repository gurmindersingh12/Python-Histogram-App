import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Custom Histogram and Bar Chart Generator")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())

    # Plot type selection (Histogram or Bar Chart)
    plot_type = st.selectbox("Select plot type", options=["Histogram", "Bar Chart"])

    # Column selection
    columns = st.multiselect("Select columns for plotting", options=data.columns[1:])

    # Custom axis labels and title
    x_label = st.text_input("X-axis label", value="Values")
    y_label = st.text_input("Y-axis label", value="Frequency" if plot_type == "Histogram" else "Count")
    title = st.text_input("Plot title", value=plot_type)

    # Font size selection
    font_size = st.slider("Font size", min_value=8, max_value=24, value=12)

    # Bar color selection
    bar_color = st.color_picker("Select bar color", "#0072B2")

    # Legend placement selection
    legend_position = st.selectbox("Select legend position", options=["upper right", "upper left", "lower right", "lower left", "center", "best"])

    if plot_type == "Histogram":
        # User input for bin size if Histogram is selected
        bins = st.slider("Select number of bins", min_value=5, max_value=100, value=30)

        # Orientation option
        orientation = st.selectbox("Select histogram orientation", options=["vertical", "horizontal"])

    if plot_type == "Bar Chart":
        # Define category ranges for the percentages
        st.write("Define the category ranges for percentage values")
        min_value = st.number_input("Minimum value for the first category", value=0, min_value=0, max_value=100)
        max_value = st.number_input("Maximum value for the last category", value=100, min_value=0, max_value=100)
        num_categories = st.slider("Select number of categories", min_value=2, max_value=10, value=4)

        # Create bins and labels dynamically
        bins = np.linspace(min_value, max_value, num_categories + 1)
        labels = [f"{int(bins[i])}-{int(bins[i+1])}%" for i in range(num_categories)]

        # Categorize the selected columns
        if len(columns) > 0:
            for column in columns:
                data[f"Category-{column}"] = pd.cut(data[column], bins=bins, labels=labels, include_lowest=True)

    # Generate plot if columns are selected
    if st.button("Generate Plot"):
        fig, ax = plt.subplots()

        if plot_type == "Histogram":
            # Plot histograms for each selected column
            for column in columns:
                ax.hist(data[column], bins=bins, alpha=0.5, label=column, orientation=orientation, color=bar_color)

        elif plot_type == "Bar Chart":
            # Plot the counts for each selected column
            for column in columns:
                category_counts = data[f"Category-{column}"].value_counts().reindex(labels, fill_value=0)
                ax.bar(category_counts.index, category_counts.values, alpha=0.7, label=column, color=bar_color)

        # Customize labels, title, and font sizes
        ax.set_xlabel(x_label, fontsize=font_size)
        ax.set_ylabel(y_label, fontsize=font_size)
        ax.set_title(title, fontsize=font_size)

        # Add legend if multiple columns are plotted
        if len(columns) > 1:
            ax.legend(loc=legend_position)

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Save the plot as TIFF
        fig.savefig(f"{plot_type.lower()}_plot.tiff", format='tiff', dpi=300)

        # Provide download button for TIFF file
        with open(f"{plot_type.lower()}_plot.tiff", "rb") as file:
            st.download_button(
                label=f"Download {plot_type} as TIFF",
                data=file,
                file_name=f"{plot_type.lower()}_plot.tiff",
                mime="image/tiff"
            )
