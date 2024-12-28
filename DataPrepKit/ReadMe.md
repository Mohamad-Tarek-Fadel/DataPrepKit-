# DataPrepKit

## Overview
DataPrepKit is a comprehensive Python toolkit for preprocessing datasets efficiently. It provides utilities for:
- Reading data from various file formats (CSV, Excel, JSON).
- Summarizing datasets with key metrics.
- Handling missing values using customizable strategies.
- Encoding categorical data into numerical formats.
- Visualizing numerical data distributions using Matplotlib.

## Features
1. **Data Reading**:
   - Supports file formats: CSV, Excel (.xls, .xlsx), and JSON.
   - Automatically detects the file type based on the file extension.

2. **Data Summarization**:
   - Computes key metrics such as mean, mode, median, and null value counts.

3. **Handling Missing Values**:
   - Options to fill missing values with mean, median, or mode.
   - Ability to drop rows with missing values.

4. **Categorical Data Encoding**:
   - Supports one-hot encoding and label encoding.

5. **Data Visualization**:
   - Visualizes the distribution of numerical data using histograms.

## Installation
### Prerequisites
- Python 3.7+
- Required libraries:
  ```bash
  pip install pandas numpy matplotlib
  ```

## Usage
### Example Workflow
1. **Reading Data**:
   ```python
   toolkit = DataPrepKit()
   data_people = toolkit.read_data("D:\\Alcamp\\DataPrepKit\\people.csv")
   ```

2. **Summarizing Data**:
   ```python
   toolkit.summarize_data(data_people)
   ```

3. **Handling Missing Values**:
   ```python
   data_people = toolkit.handle_missing_values(data_people, strategy='mean')
   ```

4. **Encoding Categorical Data**:
   ```python
   data_people = toolkit.encode_categorical_data(data_people, column='Gender', encoding_type='one_hot')
   ```

5. **Visualizing Data**:
   ```python
   toolkit.plot_numeric_distribution(data_people, column='Age')
   ```

## Project Structure
```
D:\Alcamp\DataPrepKit\
├── DataPrepKit.py        # Main Python script for the toolkit
├── people.csv            # Example dataset: People data
├── sales.csv             # Example dataset: Sales data
├── weather.csv           # Example dataset: Weather data
└── README.md             # Project documentation
```

## Functions
### `read_data(file_path: str)`
Reads data from a file and returns a Pandas DataFrame.
- **Args**: `file_path` (str): Path to the file.
- **Returns**: Pandas DataFrame.

### `summarize_data(data: pd.DataFrame)`
Prints and returns statistical summaries of the dataset.
- **Args**: `data` (Pandas DataFrame).
- **Returns**: Dictionary of summaries.

### `handle_missing_values(data: pd.DataFrame, strategy: str = 'mean', column: str = None)`
Handles missing values in the dataset.
- **Args**:
  - `data`: Dataset to process.
  - `strategy`: Strategy for handling missing values ('mean', 'median', 'mode', 'drop').
  - `column`: Specific column to apply the strategy on (optional).
- **Returns**: Processed DataFrame.

### `encode_categorical_data(data: pd.DataFrame, column: str, encoding_type: str = 'one_hot')`
Encodes categorical data into numerical formats.
- **Args**:
  - `data`: Dataset to process.
  - `column`: Column to encode.
  - `encoding_type`: Encoding type ('one_hot', 'label').
- **Returns**: Processed DataFrame.

### `plot_numeric_distribution(data: pd.DataFrame, column: str)`
Plots the distribution of numerical data in a given column.
- **Args**:
  - `data`: Dataset to process.
  - `column`: Numerical column to visualize.

## Example Output
### Processed People Data:
```
   ID     Name  Age Country  Salary  Gender_Female  Gender_Male
0   1  Ahmed_1   45   Egypt    3875           True        False
1   2  Ahmed_2   25   Egypt    5319          False         True
2   3  Ahmed_3   53   Egypt   12272           True        False
3   4  Ahmed_4   51   Egypt   14820           True        False
4   5  Ahmed_5   41   Egypt    4716          False         True
```

### Visualization Example:
![Age Distribution](#)

## License
This project is licensed under the MIT License.

