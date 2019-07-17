import unittest
from intents import Intents


class TestIntents(unittest.TestCase):
    def test_process_requests(self):
        """ Tests Hello intent response """
        expected = {'outputSpeech': {'text': 'Hello John Smith', 'type': 'PlainText'}, 'shouldEndSession': True}
        intents = Intents()
        result = intents.Hello({'name': {'value': 'John Smith'}})

        self.assertEqual(result, expected)
        self.assertEqual(type(result), dict)


if __name__ == '__main__':
    unittest.main()
