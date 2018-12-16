from marsrovers.rover import Rover
from marsrovers.parser import Parser

if __name__ == '__main__':
    for (plateau, rover_position, commands) in Parser.read_input():
        rover = Rover(plateau, rover_position)
        for command in commands:
            rover.execute(command)

        print(rover.position.x, 
              rover.position.y,
              rover.position.direction.value)