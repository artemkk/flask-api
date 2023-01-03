import flask
from flask import request, jsonify
import pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/flask-api/v1/resources/compression/all', methods=['GET'])
def api_all():
    
    conn = pymysql.connect(host="artemkk.mysql.database.azure.com", port=3306, database="concrete", user="azureuser", passwd="Ensiferum1994!", ssl={"fake_flag_to_enable_tls":True})
    conn.row_factory = dict_factory

    cur = conn.cursor()
    cur.execute('SELECT * FROM compressive_strength;')

    all_cretes = cur.fetchall()

    return jsonify(all_cretes)

app.run()
