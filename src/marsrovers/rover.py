from .command import NorthCommand, SouthCommand, WestCommand, WestCommand, CommandNotFound


class Rover:
    def __init__(self):
        self._commands = [NorthCommand(), SouthCommand(), WestCommand(), WestCommand(), RotateRightCommand(),
                          RotateLeftCommand(), CommandNotFound()]

    def move(self):
        command = filter(lambda c: c.match(self.position.direction), commands)
        new_position = command.move(self.position)
