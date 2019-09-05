"""
Problem statement
-----------------
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.


Solution
--------
The solution to this problem involves understanding the recursion behind the computation for total number of ways of decoding.

First of all, each decoded letter can either have a '1-digit' code or a '2-digit' code (<= 26). We can know the number of ways
of decoding the string before the current digit and the string before 2-digit code including the current digit. The two numbers
added together give us the number of ways of decoding the string until the current digit. This gives us the recurrence relation:
    f(x) = f(x - 1) + f(x - 2)

I will try and explain this using an example:

Input: '11312'
Algorithm:
- We start by taking the prefix string '1'. The number of ways of decoding for this string is 1. Let's maintain an array
  where we store the number of decodings until index i. Hence, arr[0] = 1

  def num_decodings(x):
    if len(x) == 1:
      if x[0] > '0':
        return 1

- The next string: '11'. The number of ways of decoding this string would be 1 (which is number of ways of decoding '1') +
  1 if this two digit string is <= '26' else 0 => hence, arr[1] = 2

  def num_decodings(x):
    if len(x) == 1:
      if x[0] > '0':
        return 1
    elif len(x) == 2:
      if x[0] < '3' and x[0] > '0' and x[1] < '7':
        if x[1] > '0':
          return 2
        else:
          return 1

- Now, our next string is: '113'. This is where our recurrence relation starts applying - the first two parts were trivial
  solutions. Basically, if all digits are valid, arr[i] += arr[i-1] + arr[i-2]. We will do this in two stages:
  (a) if our previous digit is > '0', then we can add the number of decodings of string until i-1 to our current
  count. This is because if we have '0', no next digit can be added or combined with it to add a valid decoding at the current
  position (ex: '1101'. '01' is not valid and only consideration is '(1)(10)(1)'),
  (b) if our previous digit is '1' or previous digit combined with current digit is <= '26', we can add the number of decodings
  of string until i-2.
  So for '113', '3' > '0' so we take arr[2] = arr[1] = 2. Now, if we combine '1' and '3', we get a valid two-digit code that
  can be decoded to a character, hence we add to arr[2] the number of decodings until arr[0]. So, arr[2] += arr[0].
  arr[2] = 3 finally.

- Next string is: '1131'. Here, '1' > '0', so arr[3] = arr[2] = 3. Now, '31' is not a valid two-digit code. Hence, arr[3] = 3.
- Next string is: '11312'. '2' > '0', so arr[4] = arr[3] = 3. '12' is a valid two-digit code and hence arr[4] += arr[2].
  Which gives us, arr[4] = 6 and that's the answer.

  def num_decodings(x):
    if len(x) == 1:
      if x[0] > '0':
        return 1
    elif len(x) == 2:
      if x[0] == '1' or (x[0] == '2' and x[1] < '7'):
        if x[1] > '0':
          return 2
        else:
          return 1
    else:
      arr = [0] * (len(x))
      if x[0] > '0':
        arr[0] = 1
      else:
        return 0
      if x[0] == '1' or (x[0] == '2' and x[1] < '7'):
        if x[1] > '0':
          arr[1] = 2
        else:
          arr[1] = 1

      for i in range(2, len(x)):
        if x[i] > '0':
          arr[i] += arr[i-1]
        if x[i-1] == '1' or (x[i-1] == '2' and x[i] < '7'):
          arr[i] += arr[i-2]

      return arr[-1]
"""


class Problem7(object):

    def __init__(self,
            name):
        self.name = name

    # Complexity: O(n), extra space O(n)
    def solver_num_decodings(self, x):
        if len(x) == 1:
            if x[0] > '0':
                return 1
        elif len(x) == 2:
            if x[0] == '1' or (x[0] == '2' and x[1] < '7'):
                if x[1] > '0':
                    return 2
                else:
                    return 1
        else:
            arr = [0] * (len(x))
            if x[0] > '0':
                arr[0] = 1
            else:
                return 0
            if x[0] == '1' or (x[0] == '2' and x[1] < '7'):
                if x[1] > '0':
                    arr[1] = 2
                else:
                    arr[1] = 1
            
            for i in range(2, len(x)):
                if x[i] > '0':
                    arr[i] += arr[i-1]
                if x[i-1] == '1' or (x[i-1] == '2' and x[i] < '7'):
                    arr[i] += arr[i-2]

            print("The Dynamic Program solutions array: {}".format(arr))
            return arr[-1]

    def __repr__(self):
        return "Problem #7 [Medium]: " + self.name + "\nThis problem was asked by Facebook"

if __name__ == '__main__':
    p = Problem7('Find the number of decodings for a given digit string')
    print(p)
    
    x = input("Enter the message string: ")
    numbers = []
    for ch in x:
        numbers.append(ch)

    print("Solution from solver that uses one-pass and extra O(n) space: {}".format(p.solver_num_decodings(numbers)))
