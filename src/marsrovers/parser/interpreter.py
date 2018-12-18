SPACE = ' '


class Interpreter:
    def __init__(self, content):
        self.content = content

    def interpret(self):
        raise Exception("Abstract class, implement it!")


class SpaceInterpreter(Interpreter):
    def interpret(self):
        return content.split(SPACE)


class CommandsInterpreter(Interpreter):
    def interpret(self):
        return list(content)
