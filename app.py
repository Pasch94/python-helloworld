import json
import logging

from flask import Flask

app = Flask(__name__)
logger = None # type: logging.logger

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/metrics")
def metrics():
    logger.info('metrics endpoint was reached')
    response = app.response_class(
                response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
                status=200,
                mimetype='application/json'
                )
    return response

@app.route("/status")
def status():
    logger.info('status endpoint was reached')
    response = app.response_class(
                response=json.dumps({"result":"OK - healthy"}),
                status=200,
                mimetype='application/json'
                )
    return response

if __name__ == "__main__":
    logging.basicConfig(
            filename='app.log', 
            level=10 # DEBUG
            )
    logger = logging.getLogger(__name__)
    app.run(host='0.0.0.0')
