import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataPrepKit:

    @staticmethod
    def read_data(file_path: str):
        try:
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith(('.xls', '.xlsx')):
                return pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                return pd.read_json(file_path)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV, Excel, or JSON file.")
        except Exception as e:
            raise FileNotFoundError(f"Error reading file: {e}")

    @staticmethod
    def summarize_data(data: pd.DataFrame):
        summary = {
            'mean': data.mean(numeric_only=True),
            'mode': data.mode().iloc[0].to_dict(),
            'median': data.median(numeric_only=True),
            'null_values': data.isnull().sum().to_dict()
        }
        print("Dataset Summary:")
        for key, value in summary.items():
            print(f"{key.capitalize()}:\n{value}\n")
        return summary

    @staticmethod
    def handle_missing_values(data: pd.DataFrame, strategy: str = 'mean', column: str = None):
        if strategy not in ['mean', 'median', 'mode', 'drop']:
            raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', or 'drop'.")

        if strategy == 'drop':
            return data.dropna()

        if column:
            if column not in data.columns:
                raise KeyError(f"Column '{column}' not found in the dataset.")
            if strategy == 'mean':
                data[column].fillna(data[column].mean(), inplace=True)
            elif strategy == 'median':
                data[column].fillna(data[column].median(), inplace=True)
            elif strategy == 'mode':
                data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            for col in data.columns:
                if data[col].isnull().any():
                    if strategy == 'mean':
                        data[col].fillna(data[col].mean(), inplace=True)
                    elif strategy == 'median':
                        data[col].fillna(data[col].median(), inplace=True)
                    elif strategy == 'mode':
                        data[col].fillna(data[col].mode()[0], inplace=True)
        return data

    @staticmethod
    def encode_categorical_data(data: pd.DataFrame, column: str, encoding_type: str = 'one_hot'):
        if column not in data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")

        if encoding_type == 'one_hot':
            if data[column].nunique() > 100:
                raise ValueError(f"Column '{column}' has too many unique values for one-hot encoding. Consider label encoding instead.")
            encoded = pd.get_dummies(data[column], prefix=column)
            data = pd.concat([data, encoded], axis=1).drop(column, axis=1)
        elif encoding_type == 'label':
            data[column] = data[column].astype('category').cat.codes
        else:
            raise ValueError("Invalid encoding type. Choose from 'one_hot' or 'label'.")
        return data

    @staticmethod
    def plot_numeric_distribution(data: pd.DataFrame, column: str):
        if column not in data.columns:
            raise KeyError(f"Column '{column}' not found in the dataset.")
        if not np.issubdtype(data[column].dtype, np.number):
            raise ValueError(f"Column '{column}' is not numeric and cannot be plotted.")

        plt.figure(figsize=(8, 6))
        plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    toolkit = DataPrepKit()
    base_path = "D:\\Alcamp\\DataPrepKit\\"

    try:
        data_people = toolkit.read_data(base_path + 'people.csv')
        data_sales = toolkit.read_data(base_path + 'sales.csv')
        data_weather = toolkit.read_data(base_path + 'weather.csv')

        print("People Data Summary:")
        toolkit.summarize_data(data_people)

        print("\nSales Data Summary:")
        toolkit.summarize_data(data_sales)

        print("\nWeather Data Summary:")
        toolkit.summarize_data(data_weather)

        data_people = toolkit.handle_missing_values(data_people, strategy='mean')
        data_sales = toolkit.handle_missing_values(data_sales, strategy='mean')
        data_weather = toolkit.handle_missing_values(data_weather, strategy='mean')

        data_people = toolkit.encode_categorical_data(data_people, column='Gender', encoding_type='one_hot')
        data_sales = toolkit.encode_categorical_data(data_sales, column='Product', encoding_type='one_hot')
        data_weather = toolkit.encode_categorical_data(data_weather, column='Condition', encoding_type='one_hot')

        print("\nProcessed People Data:")
        print(data_people.head())

        print("\nProcessed Sales Data:")
        print(data_sales.head())

        print("\nProcessed Weather Data:")
        print(data_weather.head())

        toolkit.plot_numeric_distribution(data_people, column='Age')
        toolkit.plot_numeric_distribution(data_sales, column='Price')
        toolkit.plot_numeric_distribution(data_weather, column='Temperature')

    except Exception as e:
        print(f"An error occurred: {e}")
