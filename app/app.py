import os
from flask import render_template, request, send_file, abort
from flask import Flask
import json
import os.path
from os import path

app = Flask(__name__)

@app.route('/insert', methods=["POST"])
def insert():
    data = {}
    data['aluno'] = []

    if path.exists("/tmp/inovacao/back-app/data.txt"):
        with open('/tmp/inovacao/back-app/data.txt') as json_file:
            data = json.load(json_file)

    data['aluno'].append({
        'nome': request.form.get("nome"),
        'email': request.form.get("email")
    })

    with open('/tmp/inovacao/back-app/data.txt', 'w') as outfile:
        json.dump(data, outfile)        

    return data

@app.route('/show')
def show():
    data = {}

    if path.exists("/tmp/inovacao/back-app/data.txt"):
        with open('/tmp/inovacao/back-app/data.txt') as json_file:
            data = json.load(json_file)

    return data

@app.route("/")
@app.route("/health")
def health():
    try:
        return f"Back-app  in ns {os.environ.get('ambiente')}: Ok!"
    except FileNotFoundError:
        abort(404)

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)