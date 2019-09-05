class Problem12(object):

    def __init__(self,
                 name):
        self.name = name

    def solver_dp(self, N, steps=[1,2]):
        dp = [0] * (N + 1)
        dp[0] = 1

        for i in range(1, N+1):
            val = 0
            for j in steps:
                if (i - j) >= 0:
                    val += dp[i-j]
            dp[i] = val

        return dp[N] 
    
    def __repr__(self):
        return "Problem #12 [Hard]: " + self.name + "\nThis problem was asked by Amazon"

if __name__ == '__main__':
    p = Problem12('Given number of steps and allowed steps at a time, find number of ways to climb')
    print(p)

    N = input("Enter the number of steps: ")
    N = int(N)
    x = input("Enter the steps allowed (space separated): ")
    x = [int(x) for x in x.split()]

    num_ways = getattr(p, 'solver_dp')

    print("Number of ways in which we can climb the steps: {}".format(num_ways(N, x)))
