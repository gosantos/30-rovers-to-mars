from marsrovers.rover import Rover
from marsrovers.parser import Parser

if __name__ == '__main__':
    for (plateau, rover_position, commands) in Parser.read_input():
        # print(plateau, rover_position, commands)
        rover = Rover(plateau, rover_position)
        for command in commands:
            rover.execute(command)

        print(rover._position.x, 
              rover._position.y,
              rover._position.direction.value)