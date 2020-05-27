## [Wednesday] May 27, 2020

* First problem was related to implementing the function `atoi` programatically. [String to integer](https://leetcode.com/problems/string-to-integer-atoi/).
  * This problem had a lot of edge cases due to the fact that the problem statement was defined like that.
  * Basically, cases that were the ones to watch out for were: `-   123`, `-52-`, `-+32`, etc.
  * I used two flags, one to track if a sign is already encountered and one to track if a digit has been encountered.
    * Using these flags, simple checks for whitespace, non-numeric character and sign were to be put in place.
    * However, be mindful of all the various cases.
    
* Second problem was related to checking if the number is also a Palindrome. [Palindrome number](https://leetcode.com/problems/palindrome-number/).
  * The solution was pretty straightforward where you convert the number to a string first. (num % 10 and num //= 10)
  * A negative input cannot be a palindrome.
  
* Third problem was an interesting problem. [Max area of water container](https://leetcode.com/problems/container-with-most-water/).
  * This problem's brute force solution was straightforward. However, I went on to think it is probably a DP-style solution.
  * I couldn't formulate subproblems so I gave up the DP idea. I then thought it's a greedy solution and I was on the right track.
  * Basically, we want to maximize the area. In order to do that, we need to maximize in two dimensions: one is width (indices farther away) and other is height (higher walls).
  * Hence, we start with the first dimension: we start from the indices farthest from each other.
    * To potentially increase the area, we move the pointer that has the smaller area toward the other pointer. This gives us a chance to get a higher wall (area is constrained by the lower wall).
    * We keep doing this until the pointers cross over or meet each other. By then, we have found the maximum area. 
