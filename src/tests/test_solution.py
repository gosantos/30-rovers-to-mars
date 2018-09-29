import unittest
from unittest.mock import patch

from marsrovers.rover import Rover
from marsrovers.parser import Parser


class TestSolution(unittest.TestCase):
    def test_solution(self):
        ''' This one is a beauty (altough too complex for a unit test):

        We mock the builtin input method using a text file
        and in the end, we compare one or more results with the
        expected values from the output text file...
        '''
        solution = []
        with open('./tests/mocks/input/00.txt', 'r') as mock_input_file:
            mock_input = mock_input_file.read().split('\n')
            with patch('builtins.input', side_effect=mock_input):
                for (plateau, rover_position, commands) in Parser.read_input():
                    # print(plateau, rover_position, commands)
                    rover = Rover(plateau, rover_position)
                    for command in commands:
                        rover.execute(command)

                    rover_solution = '{} {} {}'.format(rover.position.x,
                                                       rover.position.y,
                                                       rover.position.direction.value)
                    solution.append(rover_solution)
        
        with open('./tests/mocks/output/00.txt', 'r') as mock_output_file:
            mock_output = mock_output_file.read().split('\n')
            self.assertEqual(solution, mock_output)