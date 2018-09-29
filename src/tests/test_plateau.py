import unittest
from marsrovers.plateau import Plateau

class TestPlateau(unittest.TestCase):
    def test_object_instantiation(self):
        plateau = Plateau(x=1, y=2)
        self.assertIsInstance(plateau, Plateau)

    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_x_char(self):
        plateau = Plateau(x='someRandomStuff', y=2)
    
    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_negative_x(self):
        plateau = Plateau(x=-1, y=2)

    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_y_char(self):
        plateau = Plateau(x=1, y='someRandomStuff')
    
    @unittest.expectedFailure
    def test_invalid_object_instantiation_invalid_negative_y(self):
        plateau = Plateau(x=1, y=-2)

    def test_instantiation_from_valid_string(self):
        plateau = Plateau(x=1, y=2)
        str_plt = '1 2'  # x, y, and direction
        plateau_from_string = Plateau.from_string(str_plt)
        self.assertEqual(plateau, plateau_from_string)

    @unittest.expectedFailure
    def test_instantiation_from_invalid_string_with_wrong_x(self):
        str_plt = 'someRandomInt 2'  # x, y, and direction
        plateau_from_string = Plateau.from_string(str_plt)

    @unittest.expectedFailure
    def test_instantiation_from_invalid_string_with_wrong_y(self):
        str_plt = '1 someRandomInt'  # x, y, and direction
        plateau_from_string = Plateau.from_string(str_plt)
    
    @unittest.expectedFailure
    def test_instantiation_from_invalid__with_wrong_argnumber(self):
        str_plt = '1'  # x, y, and direction
        plateau_from_string = Plateau.from_string(str_plt)