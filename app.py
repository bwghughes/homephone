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
    matches = re.search("([0-9]+)", to)
    log.info("Got {}".format(matches.groups()))
    return matches.groups()[0]

@app.route("/zah3Ienga6vaereGhahqueiWo0ieva8ahtoh1phesi0miqueeh")
def phone():
    to = request.args.get("To")
    log.info("Deteched CallerID in {}".format(to))
    number = pull_out_number(to)
    return message.format(number)
     

if __name__ == "__main__":
    app.run()
