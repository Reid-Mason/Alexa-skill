class Intents:
    """ A class containing methods for all the intents the Alexa skill has.

    The method name must have the same name as the intent as the method is called by the intent name.
    Intent slots are passed directly into the method in json format using the slots argument.
    """

    def Hello(self, slots: dict) -> dict:
        """ The Hello intent sends a message saying hello with the passed name

        :param slots: List of variables passed from alexa request
        :return: The response containing the hello message
        """
        # Extracts the name value from passed alexa request
        name = slots.get('name').get('value')

        # Creates a response using the name value
        response = {'outputSpeech'    : {'text': f'Hello {name}', 'type': 'PlainText'},
                    'shouldEndSession': True}
        return response
