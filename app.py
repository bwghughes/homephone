import re
from flask import Flask, Response, request
app = Flask(__name__)

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

r = '<?xml version="1.0" encoding="UTF-8"?><Response><Dial callerId="+441283760715"><Number>{0}</Number></Dial></Response>'


@app.route("/zah3Ienga6vaereGhahqueiWo0ieva8ahtoh1phesi0miqueeh", methods=["POST"])
def call_forward():
    p = re.search("([0-9]+)", request.form['To'], re.I).groups()[0]
    log.info("Forwarding call to {}".format(p))
    return Response(r.format(p), mimetype='text/xml')

@app.route("/ping", methods=["GET"])
def ping():
    return "OK"


if __name__ == "__main__":
    app.run()
