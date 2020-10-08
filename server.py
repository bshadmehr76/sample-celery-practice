from flask import Flask
from tasks import tasks
from celery.result import AsyncResult
from flask import json
from tasks import celery


app = Flask(__name__)


@app.route('/new_pdf')
def create_new_pdf():
    res = tasks.create_pdf.delay()
    with open('pdf_status.csv.db', 'a+') as db:
        db.write(res.id + "\n")
    print(res.state)
    return 'Created job id is: ' + res.id

@app.route('/list_pdfs')
def list_pdfs():
    data = dict()
    try:
        with open('pdf_status.csv.db', 'r') as db:
            for line in db.readlines():
                res = celery.app.AsyncResult(line.strip())
                data[line.strip()] = res.state
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps({'error': "No file found"}),
            status=500,
            mimetype='application/json'
        )
    return response


@app.route('/ping_check_status')
def ping_check_status():
    data = dict()
    try:
        with open('ping_status.csv.db', 'r') as db:
            for line in db.readlines():
                l = line.strip().split(',')
                data[l[0]] = l[1]
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps({'error': "No file found"}),
            status=500,
            mimetype='application/json'
        )
    return response
