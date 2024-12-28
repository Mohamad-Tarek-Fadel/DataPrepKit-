import pandas as pd
import random

def generate_large_datasets():
    data_people = {
        "ID": [i for i in range(1, 101)],
        "Name": [f"Ahmed_{i}" for i in range(1, 101)],
        "Age": [random.randint(18, 60) for _ in range(100)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(100)],
        "Country": ["Egypt" for _ in range(100)],
        "Salary": [random.randint(3000, 15000) for _ in range(100)]
    }

    data_sales = {
        "TransactionID": [i for i in range(1, 201)],
        "Product": [random.choice(["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]) for _ in range(200)],
        "Quantity": [random.randint(1, 5) for _ in range(200)],
        "Price": [random.randint(100, 2000) for _ in range(200)],
        "Date": pd.date_range(start="2023-01-01", periods=200, freq="D").strftime('%Y-%m-%d').tolist()
    }

    data_weather = {
        "City": [random.choice(["Cairo", "Alexandria", "Giza", "Mansoura", "Luxor"]) for _ in range(50)],
        "Date": pd.date_range(start="2023-01-01", periods=50, freq="D").strftime('%Y-%m-%d').tolist(),
        "Temperature": [random.uniform(10.0, 40.0) for _ in range(50)],
        "Humidity": [random.randint(20, 100) for _ in range(50)],
        "Condition": [random.choice(["Sunny", "Rainy", "Cloudy", "Stormy"]) for _ in range(50)]
    }

    df_people = pd.DataFrame(data_people)
    df_sales = pd.DataFrame(data_sales)
    df_weather = pd.DataFrame(data_weather)

    df_people.to_csv("people.csv", index=False)
    df_sales.to_csv("sales.csv", index=False)
    df_weather.to_csv("weather.csv", index=False)

    df_people.to_json("people.json", orient="records", lines=False)
    df_sales.to_json("sales.json", orient="records", lines=False)
    df_weather.to_json("weather.json", orient="records", lines=False)

    df_people.to_excel("people.xlsx", index=False)
    df_sales.to_excel("sales.xlsx", index=False)
    df_weather.to_excel("weather.xlsx", index=False)

    print("Datasets generated and saved successfully!")

generate_large_datasets()
