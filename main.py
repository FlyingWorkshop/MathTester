from pathlib import Path
import json
from enum import Enum
import time

from numpy.random import default_rng

RNG = default_rng()

SENTINEL = "quit"
OPERATIONS = ("a", "s", "m", "d")


class Problem:
    def __init__(self, operation, domain: tuple[int]):
        assert operation in OPERATIONS
        assert len(domain) == 4

        a = RNG.integers(domain[0], domain[1])
        b = RNG.integers(domain[2], domain[3])
        self.n1 = max(a, b)
        self.n2 = min(a, b)
        self.operation = operation
        self.answer = None
        self.guesses = []
        self.start_time = None
        self.end_time = None
        self.correct = False

    def _make_answer(self, operation, domain):
        if operation == "a":
            return self.n1 + self.n2
        elif operation == "s":
            return self.n1 - self.n2
        elif operation == "d":
            return self.n1 / self.n2

    def attempt(self):
        print(f"")
        self.start_time = time.time()
        while not self.correct:
            guess = input()
            if guess == SENTINEL:
                break
            elif not guess.isnumeric():
                print(f"{guess} isn't numeric!")
            else:
                guess = int(guess)
                self.guesses.append(guess)
                self.correct = guess == self.answer
        self.end_time = time.time()


class Game:
    ADD_RANGE = ((2, 100), (2, 100))
    SUB_RANGE = ((2, 100), (2, 100))
    MUL_RANGE = ((2, 12), (2, 100))
    DIV_RANGE = ((2, 12), (2, 100))
    SENTINEL = "quit"

    def __init__(self, add_range=ADD_RANGE, sub_range=SUB_RANGE, mul_range=MUL_RANGE, div_range=DIV_RANGE):
        self.add_range = add_range
        self.sub_range = sub_range
        self.mul_range = mul_range
        self.div_range = div_range

        self.incorrect = set()
        self.correct = set()


    def _make_rand_add_question(self):
        rand_in


    def _make_rand_questions(self):
        yield


    def menu(self):
        print("Welcome to Math Tester! Please select (1) 2:00 minute or (2) endless mode")


    def save(self):
        pass




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.save()