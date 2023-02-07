import flask
from flask import request, jsonify
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/flask-api/v1/resources/compression/all', methods=['GET'])
def api_all():

    #establishing the connection
    conn = psycopg2.connect(database="flask-api", user='postgres', password='O55yrocks1970!', host='127.0.0.1', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Retrieving data
    cursor.execute('''SELECT * FROM Public."Concrete_Strength"''')

    #Fetching 1st row from the table
    result = cursor.fetchall();

    return jsonify(result)

app.run()
