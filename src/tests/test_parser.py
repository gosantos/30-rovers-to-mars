import unittest
from marsrovers.parser import Parser
from marsrovers.rover import RoverCommand


class TestParser(unittest.TestCase):
    def test_read_input(self):
        print('to test input parsing I would need to mock the input stream...')
        return True

    def test_commands_parsing(self):
        commands_str = 'lmrlmrlmrlmrlmrlmr'
        commands = Parser.parse_commands(commands_str)
        for command in commands:
            self.assertIsInstance(command, RoverCommand)

    @unittest.expectedFailure
    def test_invalid_commands_parsing(self):
        commands_str = 'someRandomCommandCharacters'
        commands = Parser.parse_commands(commands_str)
        for command in commands:
            self.assertIsInstance(command, RoverCommand)