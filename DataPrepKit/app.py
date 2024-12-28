from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
BASE_PATH = "d:/Alcamp/DataPrepKit/"

@app.route('/')
def index():
    # List CSV, JSON, and Excel files
    data_files = [f for f in os.listdir(BASE_PATH) if f.endswith(('.csv', '.json', '.xlsx'))]
    return render_template('index.html', files=data_files)

@app.route('/load_data', methods=['POST'])
def load_data():
    filename = request.form.get('filename')
    filepath = os.path.join(BASE_PATH, filename)
    
    try:
        # Read the data file
        if filename.endswith('.csv'):
            data = pd.read_csv(filepath)
        elif filename.endswith('.json'):
            data = pd.read_json(filepath)
        elif filename.endswith(('.xls', '.xlsx')):
            data = pd.read_excel(filepath)
        else:
            raise ValueError("Unsupported file format")
        
        # Prepare comprehensive summary
        summary = {
            'filename': filename,
            'columns': list(data.columns),
            'shape': data.shape,
            'dtypes': data.dtypes.to_dict(),
            'data_preview': data.head(10).to_dict(orient='records'),
            'statistical_summary': {}
        }
        
        # Generate statistical summary for numeric columns
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        if not numeric_columns.empty:
            summary['statistical_summary'] = data[numeric_columns].describe().to_dict()
        
        return render_template('data_summary.html', summary=summary)
    
    except Exception as e:
        # Improved error handling
        error_message = f"Error loading file {filename}: {str(e)}"
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)