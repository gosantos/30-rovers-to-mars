import unittest
from marsrovers.plateau import Plateau
from marsrovers.position import Position, Direction
from marsrovers.rover import Rover


class TestRover(unittest.TestCase):
    def test_object_instantiation(self):
        plateau = Plateau(x=10, y=10)
        position = Position(x=10, y=10, direction=Direction.NORTH)
        rover = Rover(plateau, position)
        self.assertIsInstance(rover, Rover)

    @unittest.expectedFailure
    def test_invalid_object_instantiation_wrong_plateau_object(self):
        lateau = (5, 5)
        position = Position(x=10, y=10, direction=Direction.NORTH)
        rover = Rover(plateau, position)

    @unittest.expectedFailure
    def test_invalid_object_instantiation_wrong_position_object(self):
        lateau = Plateau(x=10, y=10)
        position = (5, 5, 'n')
        rover = Rover(plateau, position)

    def test_rotation_left(self):
        plateau = Plateau(x=10, y=10)
        position = Position(x=10, y=10, direction=Direction.NORTH)
        rover = Rover(plateau, position)
        rover.rotate_left()
        self.assertEqual(rover.position.direction, Direction.WEST)

    def test_rotation_right(self):
        plateau = Plateau(x=10, y=10)
        position = Position(x=10, y=10, direction=Direction.NORTH)
        rover = Rover(plateau, position)
        rover.rotate_right()
        self.assertEqual(rover.position.direction, Direction.EAST)

    def test_movement_out_of_boundaries(self):
        plateau = Plateau(x=10, y=10)
        position = Position(x=10, y=0, direction=Direction.NORTH)
        rover = Rover(plateau, position)
        rover.move_forward()

    @unittest.expectedFailure
    def test_invalid_movement_out_of_boundaries(self):
        plateau = Plateau(x=10, y=10)
        position = Position(x=10, y=10, direction=Direction.NORTH)
        rover = Rover(plateau, position)
        rover.move_forward()
