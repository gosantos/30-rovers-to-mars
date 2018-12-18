from unittest import TestCase
from src.marsrovers.parser.interpreter import CommandsInterpreter, SpaceInterpreter


class TestInterpreter(TestCase):
    def test_space_interpreter_for_plateau(self):
        space_interpreter = SpaceInterpreter()
        interpreted_data = space_interpreter.interpret('5 5')

        self.assertEquals(interpreted_data, ['5', '5'])

    def test_space_interpreter_for_initial_rover_position(self):
        space_interpreter = SpaceInterpreter()
        interpreted_data = space_interpreter.interpret('1 2 N')

        self.assertEquals(interpreted_data, ['1', '2', 'N'])

    def test_left_right_interpreter(self):
        command_interpreter = CommandsInterpreter()
        interpreted_data = command_interpreter.interpret('LMLMLMLMM')

        self.assertEquals(interpreted_data, ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M'])

    def test_foo(self):
        num = [1, 2, 3]
        color = ['red', 'while', 'black']

        for (a, b) in zip(num, color):
            print(a)
            print(b)




