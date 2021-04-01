from collections import namedtuple
from typing import List
from copy import copy

Statement = namedtuple('Statement', ['instruction', 'argument'])


def read_program(lines):
    split_line = [line.split(" ") for line in lines]
    return [Statement(instruction, int(value)) for instruction, value in split_line]


def swap_statement(statement):
    new_instruction = "acc"
    if statement.instruction == "jmp":
        new_instruction = "nop"
    elif statement.instruction == "nop":
        new_instruction = "jmp"

    return Statement(new_instruction, statement.argument)


def get_program_mutations(program):
    for index, instruction in enumerate(program):
        new_program = copy(program)
        new_program[index] = swap_statement(new_program[index])
        yield new_program


def solve1(input):
    program = read_program(input.splitlines())
    game = GameConsole(program)
    try:
        game.boot()
    except ValueError:
        return game.state.accumulator


def solve2(input):
    program = read_program(input.splitlines())
    for program_candidate in get_program_mutations(program):
        game = GameConsole(program_candidate)
        try:
            return game.boot()
        except ValueError:
            pass


class State:
    def __init__(self):
        self.accumulator = 0
        self.statement_pointer = 0


class GameConsole:
    program: List[Statement]
    state: State

    def __init__(self, program):
        self.program = program
        self.state = State()

    def nop(self, argument):
        self.state.statement_pointer += 1

    def acc(self, argument):
        self.state.statement_pointer += 1
        self.state.accumulator += argument

    def jmp(self, argument):
        self.state.statement_pointer += argument

    def run_state(self):
        current_statement = self.program[self.state.statement_pointer]
        transition = getattr(self, current_statement.instruction)
        transition(current_statement.argument)

    def boot(self):
        executed_statements = set()
        while self.state.statement_pointer < len(self.program):
            self.run_state()
            if self.state.statement_pointer in executed_statements:
                raise ValueError("infinite loop detected")
            executed_statements.add(self.state.statement_pointer)
        return self.state.accumulator
