from .logger import Logger

class Solver(object):

    def __init__(self,
                 pnum,
                 desc,
                 company,
                 category,
                 level,
                 logging=True):

        self.problem_number = pnum
        self.description = desc
        self.askedBy = company
        self.category = category
        self.logging = logging

        self.log = Logger(pnum, company, category, level)

    # The function for the best solution for each problem.
    # To have more solutions, add more functions to the
    # problem class itself.
    def solve(self, x, **kwargs):
        raise NotImplementedError

    # The function (a bit ambitious) that interprets the
    # algorithm, in a way dry running it and printing out
    # useful information to understand what is going on.
    def interpret(self, x, **kwargs):
        raise NotImplementedError

    # A private function to get the logger instance so that
    # it can be used in the interpret function
    def _get_logger(self):
        return self.log

    # A private function that returns the solver for the
    # problem (used to hide the actual function name)
    def _get_solver(self):
        return self.solve
    
    # A private function that returns the interpreter for the
    # problem (used to hide the actual function name)
    def _get_interpreter(self):
        return self.interpret

    def print_description(self):
        print(self.description)
