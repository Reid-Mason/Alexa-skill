import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_process_requests(self):
        """ Tests adding headers to responses """
        expected = '{"version": "1.0", "response": {"outputSpeech": {"text": "Hello World!"}}, "sessionAttributes": ""}'
        result = utils.add_response_headers({'outputSpeech': {'text': 'Hello World!'}})
        
        self.assertEqual(result, expected)
        self.assertEqual(type(result), str)


if __name__ == '__main__':
    unittest.main()
