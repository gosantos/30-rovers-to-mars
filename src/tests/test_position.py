import unittest
from marsrovers.position import Position


class TestPosition(unittest.TestCase):
    def test_object_instantiation(self):
        pos = Position(x=1, y=2, direction='n')
        self.assertIsInstance(pos, Position)

    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_x(self):
        pos = Position(x='notIntValue', y=2, direction='n')
    
    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_y(self):
        pos = Position(x=1, y='notIntValue', direction='n')
    
    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_direction(self):
        pos = Position(x=1, y='notIntValue', direction='z')

    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_direction2(self):
        pos = Position(x=1, y='notIntValue', direction=1)


    def test_instantiation_from_valid_string(self):
        pos = Position(x=1, y=2, direction='n')
        str_pos = '1 2 n'  # x, y, and direction
        position_from_string = Position.from_string(str_pos)
        self.assertEqual(pos, position_from_string)

    @unittest.expectedFailure
    def test_instantiation_from_invalid_string_with_wrong_xy(self):
        str_pos = 'someRandomInt 2 n'  # x, y, and direction
        position_from_string = Position.from_string(str_pos)

    @unittest.expectedFailure
    def test_instantiation_from_invalid_string_with_wrong_direction(self):
        str_pos = '1 2 someInvalidCharacter'  # x, y, and direction
        position_from_string = Position.from_string(str_pos)
    
    @unittest.expectedFailure
    def test_instantiation_from_invalid__with_wrong_argnumber(self):
        str_pos = '1 2'  # x, y, and direction
        position_from_string = Position.from_string(str_pos)