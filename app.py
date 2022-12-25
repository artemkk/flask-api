import flask
from flask import request, jsonify
import pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

compression = [
    {'id': 0,
     'cement': '540',
     'blast_furnace_slag': '0',
     'fly_ash': '0',
     'water': '162',
     'superplasticizer': '0',
     'coarse_aggregate': '1040',
     'fine_aggregate': '676',
     'age': '28',
     'strength': '79.99'},
    {'id': 1,
     'cement': '540',
     'blast_furnace_slag': '0',
     'fly_ash': '0',
     'water': '162',
     'superplasticizer': '2.5',
     'coarse_aggregate': '1055',
     'fine_aggregate': '676',
     'age': '28',
     'strength': '61.89'},
    {'id': 2,
     'cement': '332.5',
     'blast_furnace_slag': '142.5',
     'fly_ash': '0',
     'water': '228',
     'superplasticizer': '2.5',
     'coarse_aggregate': '932',
     'fine_aggregate': '594',
     'age': '28',
     'strength': '40.27'}
]

@app.route('/flask-api/v1/resources/compression/all', methods=['GET'])
def api_all():
    return jsonify(compression)


@app.route('/flask-api/v1/resources/compression', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for elem in compression:
        if elem['id'] == id:
            results.append(elem)

    return jsonify(results)

app.run()
