COMMANDS = 'commands'
INITIAL_POSITIONS = 'initial_positions'
PLATEAU = 'plateau'

INITIAL_POSITION_REGEX = r'\d\s\d\s\w'
PLATEAU_REGEX = r'\d\s\d'
COMMANDS_REGEX = r'L*M*R*'


class Parser:
    def __init__(self):
        self.data = {PLATEAU: None, INITIAL_POSITIONS: [], COMMANDS: []}

    def parse(self, content):
        if re.match(PLATEAU_REGEX, content):
            space_interpreter = SpaceInterpreter(content)
            raw_plateau = space_interpreter.interpret()
            plateau = PlateauFactory(raw_plateau)
            self.data[PLATEAU] = plateau
        elif re.match(INITIAL_POSITION_REGEX, content):
            space_interpreter = SpaceInterpreter(content)
            raw_position = space_interpreter.interpret()
            position = PositionFactory(raw_position)
            self.data[INITIAL_POSITIONS].append(position)
        elif re.match(COMMANDS_REGEX, content):
            command_interpreter = CommandInterpreter(content)
            raw_command = command_interpreter.interpret()
            command = CommandFactory(raw_command)
            self.data[COMMANDS].append(command)
        else:
            raise RuntimeError("Not well formatted file")
