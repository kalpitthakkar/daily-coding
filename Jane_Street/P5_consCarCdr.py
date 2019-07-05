def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

class Problem5(object):

    def __init__(self,
                 name):
        self.name = name

    # The whole idea of this problem is functional programming.
    # Use the function cons(a, b) to understand the functional
    # interface required to write functions car(f) and cdr(f).
    # car/cdr takes a function as input => as cons(a,b) returns a
    # function. The returned function takes a function as input,
    # which has two arguments like cons => this inner function
    # like cons can be made by us according to whether it is called
    # from car or cdr.

    def solver_car(self, f):
        def first(x, y):
            return x

        return f(first)

    def solver_cdr(self, f):
        def last(x, y):
            return y

        return f(last)

    def __repr__(self):
        return "Problem #5 [Medium]: " + self.name + "\nThis problem was asked by Jane Street"

if __name__ == '__main__':
    p = Problem5('Return first element of pair using car and second using cdr')
    print(p)
    
    x = cons(2, cons(cons(3, 4), 5))
   
    car = getattr(p, 'solver_car')
    cdr = getattr(p, 'solver_cdr')

    print("Input: x = cons(2, cons(cons(3, 4), 5))")
    print("Solution from solver for car function: car(x) = {}".format(car(x)))
    print("Solution from solver for cdr function: cdr(cdr(x)) = {}".format(cdr(cdr(x))))
