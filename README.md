# Custom Histogram and Bar Chart Generator


#### Welcome to the Histogram and Bar Chart Generator! This Python-based web app allows users to easily create histograms and bar charts from their data files. Simply upload a CSV file, select the column you want to visualize, generate a visuals instantly, and download the generated plot as a high-resolution TIFF file.


### Features

1. <b>File Upload:</b> Upload your own CSV file to visualize data.</p>
2. <b>Plot Type Selection:</b> Choose between Histogram and Bar Chart.</p>
3. <b>Column Selection:</b> Choose which columns from the CSV file to visualize.</p>
4. <b>Axis Labels and Title Customization:</b> Customize x-axis label, y-axis label, and plot title.</p>
5. <b>Font Size Adjustment:</b> Control font size for axis labels and title.</p>
6. <b>Color Customization:</b> Select or enter colors for bars, with multiple options.</p>
7. <b>Legend Position:</b> Choose where to place the legend on the plot.</p>
8. <b>Category Ranges (for Bar Chart):</b> Define custom categories for percentage values.</p>
9. <b>Orientation Selection (for Histogram):</b> Choose between vertical and horizontal orientations.</p>
10. <b>Download Plot:</b> Save the plot as a high-resolution TIFF file.</p>


### Installation

To run this application, you need to have Python 3.x and Streamlit installed. Follow these steps to set up and launch the application.
Prerequisites

### Install the required libraries by running:

```
pip install streamlit pandas matplotlib numpy
```

### Running the Application

1. Clone or download this repository.
2. Open a terminal and navigate to the directory where app.py is located.
3. Run the following command:

```
streamlit run app.py
```

4. The application will open in your default web browser.


### Usage
#### A. File Upload
1. Upload your CSV file by clicking on the Upload your CSV file button.
2. Once the file is uploaded, a data preview will appear to ensure the data is loaded correctly.

#### B. Plot Type Selection
Choose the type of plot:
1. Histogram: Plots the frequency distribution of a single column.
2. Bar Chart: Displays counts for custom percentage ranges across selected columns.

#### C. Column Selection
Select one or more columns to include in the plot. Only numeric columns are eligible.


#### D. Customization Options
1. Axis Labels and Title: Customize the `X-axis` and `Y-axis` labels and add a descriptive `Plot title`.
2. Font Size: Adjust the font size for the plot elements (axis labels and title) using the slider.
3. Color Selection: Type a color name in the text input box, or Choose a predefined color from a dropdown list.
4. Legend Position: Select the position for the legend. Options include: `upper right`, `upper left`, `lower right`, `lower left`, `center`, and `best`.


    
