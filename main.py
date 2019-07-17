import json
from intents import Intents
from flask import Flask
import flask
import utils

# Initialise flask app
app = Flask(__name__)


def LaunchRequest() -> str:
    """ The handler for the skill launch request

    :return: The text to say when the skill is launched
    """
    response = {'outputSpeech'    : {'text': 'What would you like to do?', 'type': 'PlainText'},
                'shouldEndSession': False}
    # Add the response headers
    response = utils.add_response_headers(response)
    return response


@app.route('/alexa_test', methods = ['GET', 'POST'])
def process_requests() -> str:
    # Decode the data sent from the alexa
    data = json.loads(flask.request.data.decode('utf-8'))

    # Get the request data to determine what kind of request it was
    request = data.get('request')
    request_type = request.get('type')

    # When there is a launch request
    if request_type == 'LaunchRequest':
        return LaunchRequest()

    # When it is an intent request
    if request_type == 'IntentRequest':
        # Class of intent handlers
        intents = Intents()
        intent = request.get('intent')

        # Pass along any variables obtained from alexa request
        slots = None
        if 'slots' in intent:
            slots = intent.get('slots')

        # Run the corresponding intent handler
        response = getattr(intents, intent.get('name'))(slots)
        return utils.add_response_headers(response)


if __name__ == '__main__':
    app.run(debug = True)
