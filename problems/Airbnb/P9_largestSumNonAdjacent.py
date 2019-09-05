class Problem9(object):

    def __init__(self,
                 name):
        self.name = name

    """
    Using dynamic programming, the recurrence relation would be:
        1) if we include the current element, dp[i] = x[i] + dp[i+2]
        2) if we exclude the current element, dp[i] = dp[i+1]

    And our final solution is the maximum of these two values, which
    is: max(x[i] + dp[i+2], dp[i+1]).
    """
    def solver_largest_sum_dp(self, x):
        dp = [0 for _ in range(len(x))]
        visited = [False for _ in range(len(x))]

        def get_largest_sum(inp, idx, nelems):
            if idx >= nelems:
                return 0

            if visited[idx]:
                return dp[idx]
            visited[idx] = True

            dp[idx] = max(get_largest_sum(inp, idx+1, nelems),
                    inp[idx] + get_largest_sum(inp, idx+2, nelems))

            return dp[idx]

        return get_largest_sum(x, 0, len(x))

    def solver_largest_sum_non_adjacent(self, x):
        sum_incl = x[0]
        sum_excl = 0

        for i in range(1, len(x)):
            new_sum_excl = sum_incl if (sum_incl > sum_excl) else sum_excl

            sum_incl = sum_excl + x[i]
            sum_excl = new_sum_excl

        return sum_incl if (sum_incl > sum_excl) else sum_excl


    def __repr__(self):
        return "Problem #9 [Hard]: " + self.name + "\nThis problem was asked by Airbnb"

if __name__ == '__main__':
    p = Problem9("Given a list of integers, find the largest sum of non-adjacent numbers")
    print(p)

    x = input("Enter the list of numbers (space separated): ")
    x = [int(n) for n in x.split()]

    largest_sum = getattr(p, 'solver_largest_sum_non_adjacent')
    dp_largest_sum = getattr(p, 'solver_largest_sum_dp')
    print("Solution from solver for number of largest sum without having adjacent numbers (using Dynamic Programming): {}".format(dp_largest_sum(x)))
    print("Solution from solver for number of largest sum without having adjacent numbers: {}".format(largest_sum(x)))
