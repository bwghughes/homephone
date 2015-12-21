import re
from flask import Flask, jsonify, request
app = Flask(__name__)

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

message = """
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial callerId="+441283760715">
        <Number>{}</Number>
    </Dial>
</Response>
"""

def pull_out_number(to):
    matches = re.search("/:([0-9]+)@/", to)
    return matches.groups()[0]

@app.route("/zah3Ienga6vaereGhahqueiWo0ieva8ahtoh1phesi0miqueeh")
def phone():
    log.info(request.form)
    log.info(request.args)
    return jsonify(request.form)
     

if __name__ == "__main__":
    app.run()
