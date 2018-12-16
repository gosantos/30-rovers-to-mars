from unittest import TestCase
from ..marsrovers.command import NorthCommand, RotateRightCommand
from ..marsrovers.enums.directions import Commands
from ..marsrovers.position import Position


class TestCommand(TestCase):
    def test_north_command_match(self):
        north_command = NorthCommand()

        self.assertEqual(north_command.match(Commands.NORTH), True)

    def test_north_command_move(self):
        north_command = NorthCommand()

        position = Position(1, 1, Commands.NORTH)

        new_position = north_command.move(position)

        self.assertEqual(new_position.y, 2)

    def test_rotate_right_command_match(self):
        rotate_right_command = RotateRightCommand()

        self.assertEqual(rotate_right_command.match(Commands.RIGHT), True)

    def test_rotate_right_command_move(self):
        rotate_right_command = RotateRightCommand()

        position = Position(1, 1, Commands.NORTH)

        new_position = rotate_right_command.move(position)

        self.assertEqual(new_position.direction, Commands.EAST)
