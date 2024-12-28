# DataPrepKit

## Overview
DataPrepKit is a Python project designed to simplify data preprocessing and analysis tasks. It includes features for reading data, summarizing key statistics, handling missing values, encoding categorical data, and visualizing numerical data distributions through a user-friendly web interface built with Flask.

## Features
- **Data Reading**: Supports CSV, Excel, and JSON formats.
- **Data Summarization**: Provides key metrics like mean, median, mode, and null counts.
- **Handling Missing Values**: Offers flexible strategies for filling or dropping missing data.
- **Encoding Categorical Data**: Supports one-hot and label encoding for categorical columns.
- **Visualization**: Creates histograms to visualize numerical data distributions.
- **Web Interface**: Enables file selection and data summary visualization directly through a web browser.

## Setup
### Requirements
- Python 3.7+
- Libraries: Pandas, NumPy, Matplotlib, Flask

Install the required libraries using:
```bash
pip install pandas numpy matplotlib flask
```

## How It Works
### 1. Reading Data
You can load data from various file formats through the web interface or programmatically:
```python
from DataPrepKit import DataPrepKit

data = DataPrepKit.read_data("D:\\Alcamp\\DataPrepKit\\people.csv")
```

### 2. Summarizing Data
Get a quick statistical summary:
```python
DataPrepKit.summarize_data(data)
```

### 3. Handling Missing Values
Choose how to handle missing data:
```python
data = DataPrepKit.handle_missing_values(data, strategy='mean')
```

### 4. Encoding Categorical Data
Easily encode categorical columns:
```python
data = DataPrepKit.encode_categorical_data(data, column='Gender', encoding_type='one_hot')
```

### 5. Visualizing Data
Create histograms for numerical columns:
```python
DataPrepKit.plot_numeric_distribution(data, column='Age')
```

### 6. Web Interface
Launch the Flask application to interact with the data through a web browser:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` to:
- Select a data file.
- View a detailed summary, including statistical insights and data preview.
- Handle errors in file selection or processing.

## Folder Structure
```
D:\Alcamp\DataPrepKit\
├── app.py               # Flask application for the web interface
├── Data.py              # Script to generate sample data files
├── DataPrepKit.py       # Main Python library for data preprocessing
├── people.csv           # Example dataset (People data)
├── sales.csv            # Example dataset (Sales data)
├── weather.csv          # Example dataset (Weather data)
├── templates            # HTML templates for the web interface
│   ├── index.html       # File selection interface
│   ├── data_summary.html# Data summary display
│   └── error.html       # Error handling display
└── README.md            # Project documentation (this file)
```

## Flask Application
The Flask app provides a simple and intuitive web interface for interacting with datasets. It includes:
- **`/` Route**: Lists available data files and allows users to select one.
- **`/load_data` Route**: Processes the selected file and displays a comprehensive summary.

## Functions Explained
### `read_data(file_path: str)`
Reads data from a specified file path and returns a DataFrame.

### `summarize_data(data: pd.DataFrame)`
Prints and returns statistical summaries of the dataset.

### `handle_missing_values(data: pd.DataFrame, strategy: str, column: str = None)`
Handles missing values based on the chosen strategy (mean, median, mode, or drop).

### `encode_categorical_data(data: pd.DataFrame, column: str, encoding_type: str)`
Encodes categorical data using one-hot or label encoding.

### `plot_numeric_distribution(data: pd.DataFrame, column: str)`
Plots the distribution of numerical data for the specified column.

## Example Output
### Sample Processed Data
```
   ID     Name  Age Country  Salary  Gender_Female  Gender_Male
0   1  Ahmed_1   45   Egypt    3875           True        False
1   2  Ahmed_2   25   Egypt    5319          False         True
2   3  Ahmed_3   53   Egypt   12272           True        False
3   4  Ahmed_4   51   Egypt   14820           True        False
4   5  Ahmed_5   41   Egypt    4716          False         True
```

### Sample Visualization
The toolkit also generates visualizations like this for numerical columns:
```
Histogram: Distribution of Age
```

## Conclusion
This project combines data preprocessing capabilities with a web-based interface to simplify interaction with datasets. It’s a versatile tool suitable for analysts, researchers, and developers who work with structured data.

For feedback or suggestions, feel free to reach out!

