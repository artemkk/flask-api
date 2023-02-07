import flask
import psycopg2
import requests
import json
from ml_model2 import execute_model, define_model
import numpy as np

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/flask-api/v1/resources/compression/data', methods=['GET'])
def api_data():

    # Establish connection
    conn = psycopg2.connect(database="flask-api", user='postgres', password='O55yrocks1970!', host='127.0.0.1', port= '5432')

    # Set auto commit false
    conn.autocommit = True

    # Create a cursor object
    cursor = conn.cursor()

    # Retrieve data from PostgreSQL database's Concrete_Strength table
    cursor.execute('''SELECT * FROM Public."Concrete_Strength"''')

    # Fetch all from the table
    result = cursor.fetchall();

    return result

@app.route('/flask-api/v1/resources/compression/execute', methods=['GET'])
def api_model():
    
    # Retrieve Data from server
    response = requests.get('http://127.0.0.1:5000//flask-api/v1/resources/compression/data').text
    
    # Receive as JSON object
    response_info = response_info = json.loads(response)

    # Parse JSON into Numpy Array
    raw_data = np.array(response_info)

    # Split data into training and validation/testing data
    split_data = np.split(raw_data, [829])

    training_data = split_data[0]
    validation_data = split_data[1]

    # Run model
    execute_model(training_data, validation_data)

    return response_info

if __name__ == "__main__":
    app.run()
