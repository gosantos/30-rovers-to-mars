from .command import NorthCommand, SouthCommand, WestCommand, WestCommand, CommandNotFound


class Rover:
    def __init__(self, plateau, position):
        self._commands = [NorthCommand(), SouthCommand(), WestCommand(), WestCommand(), RotateRightCommand(),
                          RotateLeftCommand(), CommandNotFound()]
        self._plateau = plateau
        self.position = position

    def move(self):
        print('({}, {}) - moving forward...'.format(self.position.x,
                                                    self.position.y))

        command = filter(lambda c: c.match(self.position.direction), commands)
        new_position = command.move(self.position)

        if self._plateau.isValidPosition(new_position):
            self.position = new_position
            return self
        else:
            raise RuntimeError('Invalid move:', command)
