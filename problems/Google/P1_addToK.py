import sys
sys.path.append("../..")
from central import Solver

class Solution(Solver):

    def __init__(self,
                 pnum,
                 desc,
                 company,
                 category,
                 level,
                 logging=True):

        super(Solution, self).__init__(
            pnum, desc, company, category, level,
            logging
        )

    # Complexity: O(n^2)
    def solver_naive(self, x, k):
        for val in x:
            diff = k - val
            for rem in x:
                if diff == rem:
                    return True

        return False

    # Complexity: O(n log(n))
    def solver_better(self, x, k):
        left = 0
        right = len(x) - 1
        x = sorted(x)       # n log(n)

        found = False
        while True:
            if left >= right:
                break
            val = x[left]
            diff = k - val
            if diff == x[right]:
                found = True
                break
            elif diff > x[right]:
                left = left + 1
            elif diff < x[right]:
                right = right - 1

        return found

    def solve(self, x, **kwargs):
        k = kwargs['k']

        memory = []
        for val in x:
            diff = k - val
            if diff in memory:
                return True
            memory.append(val)

        return False

    def interpret(self, x, **kwargs):
        k = kwargs['k']

        var_to_interpret = {
            'memory': [],
            'val': [],
            'diff': [],
        }
        memory = []
        for val in x:
            diff = k - val
            mm = memory.copy()
            var_to_interpret['val'].append(val)
            var_to_interpret['diff'].append(diff)
            var_to_interpret['memory'].append(mm)
            if diff in memory:
                if self.logging:
                    self.log.flushvars(
                        vars_to_interpret=var_to_interpret,
                        num_iters=len(var_to_interpret['val']),
                        return_val=True
                    )
                return True
            memory.append(val)

        if self.logging:
            self.log.flushvars(
                vars_to_interpret=var_to_interpret,
                num_iters=len(var_to_interpret['val']),
                return_val=False
            )
        return False

if __name__ == '__main__':
    desc = ("Given a list of numbers and a number k, return whether any two numbers from the list add up to k.\n\n" +
            "For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.\n\n" +
            "Bonus: Can you do this in one pass?\n\n")
    p = Solution(
        pnum=1,
        desc=desc,
        company="Google",
        category="Number Arithmetic",
        level="Easy",
        logging=True
    )
    p.print_description()

    x = input("Enter the list of numbers (space separated): ")
    numbers = [int(n) for n in x.split()]
    k = input("Enter the value of K: ")
    k = int(k)

    solver = p._get_solver()

    print("Solution for the given input: {}".format(solver(numbers, k=k)))
    if p.logging:
        interpreter = p._get_interpreter()
        interpreter(numbers, k=k)
