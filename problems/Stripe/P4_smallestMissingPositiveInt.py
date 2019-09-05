class Problem4(object):

    def __init__(self,
                 name):
        self.name = name

    # Complexity: O(n^2)
    def solver_non_linear_time(self, x):
        max_num = -1
        for i in range(len(x)):
            max_num = max(max_num, x[i])
        found = False
        for i in range(1, max_num):
            for j in x:
                if i == j:
                    found = True
                    break
            if not found:
                return i
            found = False

    # Complexity: O(n), extra space
    def solver_extra_space_linear_time(self, x):
        visited = {}
        max_num = -1
        for i in range(len(x)):
            max_num = max(max_num, x[i])
        for i in range(len(x)):
            if x[i] > 0:
                visited[x[i]] = 1

        for i in range(1, max_num):
            if i not in visited:
                return i

    # Complexity: O(nlogn)
    def solver_log_linear_time(self, x):
        x = sorted(x)
        val = 1
        for v in x:
            if v == val:
                val += 1

        return val

    # Complexity: O(n), constant space
    def solver_constant_space_linear_time(self, x):
        j = 0
        for i in range(len(x)):
            if x[i] <= 0:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
                j += 1
        
        size = len(x) - j
        x = x[j:]
        for i in range(0, size):
            if abs(x[i]) - 1 < size and x[abs(x[i]) - 1] > 0:
                x[abs(x[i]) - 1] = -x[abs(x[i]) - 1]

        for i in range(0, size):
            if x[i] > 0:
                return i + 1

        return size + 1

    def __repr__(self):
        return "Problem #4 [Hard]: " + self.name + "\nThis problem was asked by Stripe"

if __name__ == '__main__':
    p = Problem4('Find the first positive integer missing in the array')
    print(p)
    
    x = input("Enter the list of numbers (space separated): ")
    numbers = [int(n) for n in x.split()]

    print("Solution from solver that uses non-linear time (n^2): {}".format(p.solver_non_linear_time(numbers)))
    print("Solution from solver that uses loglinear time (nlogn): {}".format(p.solver_log_linear_time(numbers)))
    print("Solution from solver that uses linear time and extra space (n): {}".format(p.solver_extra_space_linear_time(numbers)))
    print("Solution from solver that uses linear time and constant space (n): {}".format(p.solver_constant_space_linear_time(numbers)))
