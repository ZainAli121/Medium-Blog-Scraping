from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv("data.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json_data')
def json_data():
    return render_template('json_data.html')

@app.route('/search', methods=['GET'])
def search():
    print("Request args:", request.args)
    
    keyword = request.args.get('keyword', '').strip().lower()
    if not keyword:
        return jsonify({"error": "Please provide a keyword"}), 400
    
    print(df.columns)

    results = df[df['title'].str.contains(keyword, case=False, na=False)]
    data = results.replace({np.nan: None}).to_dict(orient='records')

    return jsonify({"results": data})

if __name__ == '__main__':
    app.run(debug=True)
