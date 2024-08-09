from flask import Flask, jsonify
import json

app = Flask(__name__)
FILE_PATH = 'data.json'

@app.route('/data', methods=['GET'])
def get_data():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data = [json.loads(line) for line in lines]
    
    response = jsonify(data)
    response.charset = 'utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
