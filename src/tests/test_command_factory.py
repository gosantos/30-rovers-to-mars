from unittest import TestCase
from src.marsrovers.models.command import Command, CommandFactory
from src.marsrovers.enums.commands import Commands


class TestCommandFactory(TestCase):
    def test_foo(self):
        factory_create = CommandFactory.create(list('LMR'))

        command = Command([Commands.L, Commands.M, Commands.R])

        self.assertEquals(factory_create.commands, command.commands)
