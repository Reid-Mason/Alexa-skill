import json


def add_response_headers(response: dict) -> str:
    """ Used for adding the universal headers to responses

    :param response: The main body of the response to be rapped with the header
    :return: The full response with header and response data
    """
    return json.dumps({
        'version'          : '1.0',
        'response'         : response,
        'sessionAttributes': ''
    })
