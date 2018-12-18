from ..enums.commands import Commands


class Command:
    def __init__(self, commands):
        self.commands = commands


class CommandFactory:
    @staticmethod
    def create(commands):
        return Command(list(map(lambda c: Commands[c], commands)))
