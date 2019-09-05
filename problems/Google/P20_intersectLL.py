import sys
sys.path.append("../..")
from central import Solver

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

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

    # Complexity: O(m*n)
    def solver_naive(self, x, y):
        heady = y
        while x is not None:
            while y is not None:
                if x.val == y.val:
                    return x
                y = y.nxt
            y = heady
            x = x.nxt
        return None

    # Complexity: O(m+n)
    def solve(self, x, **kwargs):
        l1 = x[0]
        l2 = x[1]

        len_l1 = 0; len_l2 = 0
        head_l1 = l1; head_l2 = l2
        while l1 is not None:
            l1 = l1.nxt
            len_l1 += 1
        while l2 is not None:
            l2 = l2.nxt
            len_l2 += 1
        
        diff = abs(len_l2 - len_l1)
        if len_l2 > len_l1:
            longer = head_l2
            shorter = head_l1
        else:
            longer = head_l1
            shorter = head_l2

        ctr = 0
        while longer is not None:
            if ctr == diff:
                break
            ctr += 1
            longer = longer.nxt
        while longer is not None:
            if longer.val == shorter.val:
                return longer
            longer = longer.nxt
            shorter = shorter.nxt
        return None

    def interpret(self, x, **kwargs):
        # TODO: Implement this
        return

if __name__ == '__main__':
    desc = ("Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.\n\n" +
	    "For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.\n\n" +
	    "In this example, assume nodes with the same value are the exact same node objects.\n\n" +
	    "Challenge: Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.\n\n")
    p = Solution(
        pnum=20,
        desc=desc,
        company="Google",
        category="Linked List",
        level="Easy",
        logging=False
    )
    p.print_description()

    def create_LL(numbers):
        head = Node(numbers[0])
        temp = head
        for i in range(1, len(numbers)):
            while head.nxt is not None:
                head = head.nxt
            head.nxt = Node(numbers[i])
        return temp

    x = input("Enter the list of numbers for Linked List 1 (space separated): ")
    numbers = [int(n) for n in x.split()]
    x = create_LL(numbers)
    y = input("Enter the list of numbers for Linked List 2 (space separated): ")
    numbers = [int(n) for n in y.split()]
    y = create_LL(numbers)

    solver = p._get_solver()

    print("Solution for the given input: {}".format(solver([x, y]).val))
    if p.logging:
        interpreter = p._get_interpreter()
        interpreter(numbers, k=k)
