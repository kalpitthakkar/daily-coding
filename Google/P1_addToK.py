class Problem1(object):

    def __init__(self,
                 name):
        self.name = name

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

    def solver_best(self, x, k):
        memory = []
        for val in x:
            diff = k - val
            if diff in memory:
                return True
            memory.append(val)

        return False

    def __repr__(self):
        return "Problem #1 [Easy]: " + self.name + "\nThis problem was asked by Google"

if __name__ == '__main__':
    p = Problem1('Two numbers in a list add up to K')
    print(p)

    x = input("Enter the list of numbers (space separated): ")
    numbers = [int(n) for n in x.split()]
    k = input("Enter the value of K: ")
    k = int(k)

    print("Solution from naive solver (n^2): {}".format(p.solver_naive(numbers, k)))
    print("Solution from better solver (n log(n)): {}".format(p.solver_better(numbers, k)))
    print("Solution from best solver (n, extra space): {}".format(p.solver_best(numbers, k)))
