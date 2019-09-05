class Problem2(object):

    def __init__(self,
                 name):
        self.name = name

    # Complexity: O(n)
    def solver_with_division(self, x):
        output = []
        prod = 1
        for val in x:
            prod *= val
        for val in x:
            output.append(prod // val)
        
        return output

    # Complexity: O(n)
    # The main idea of this solution is to use two lists which contain the partial value for
    # the final product to be calculated. This can be done by calculating a cumulative product
    # from left and right but skipping the present element while calculating the cumulative.
    # The final product will just then be product of values at each corresponding array location
    # in the two cumulative product lists.
    def solver_without_division(self, x):
        cum_prod_l = [1] * len(x)
        cum_prod_r = [1] * len(x)
        for i in range(1, len(x)):
            cum_prod_l[i] = x[i-1] * cum_prod_l[i-1]
            cum_prod_r[len(x)-1-i] = x[len(x)-i] * cum_prod_r[len(x)-i]

        output = [a*b for (a,b) in zip(cum_prod_l,cum_prod_r)]

        return cum_prod_l, cum_prod_r, output

    def __repr__(self):
        return "Problem #2 [Hard]: " + self.name + "\nThis problem was asked by Uber"

if __name__ == '__main__':
    p = Problem2('Return product of all except number in that position')
    print(p)

    x = input("Enter the list of numbers (space separated): ")
    numbers = [int(n) for n in x.split()]

    print("Solution from solver with division (n): {}".format(p.solver_with_division(numbers)))
    cum_prod_l, cum_prod_r, output = p.solver_without_division(numbers)
    print("Solution from solver without division (n): {}".format(output))
    print("Cumulative product list L: {}".format(cum_prod_l))
    print("Cumulative product list R: {}".format(cum_prod_r))
