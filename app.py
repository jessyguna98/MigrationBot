import json
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
log = app.logger


@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    #res = "Hurray!"

    if action == 'migration':
res = is_valid_doctor(req)
