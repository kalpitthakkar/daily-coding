### [Saturday] May 23, 2020

* First problem of the day was [Two Sum](https://leetcode.com/problems/two-sum/).
  * Optimal: The main idea of the solution was to identify that in order to find the complement (ressidual from target: target - current) of current number in array, you need to maintain some hash map. O(n) time complexity and O(n) space complexity.
  * Also, a solution you'd stumble upon could be: sort the array and then maintain two pointers. More time complexity O(nlogn), but gives you O(1) space complexity.
  * Brute Force: O(n^2)
  
* Second problem was related to [Linked Lists](https://leetcode.com/problems/add-two-numbers/). Add two numbers represented as linked lists (reversed order of digits).
  * First of all, the sample test case is __smart__. They gave two linked lists of equal length. This right away tricks you into thinking the two numbers have same number of digits -- but nowhere has it been mentioned that's the case.
  * I fell for that but caught my mistake right away and started building rest of the solution. It was a simple extension of same length numbers addition.
  * The only edge case is: If the last addition in the sequence generates a carry -- the number of digits in the sum is one greater than number of digits in the larger list.
  * __Fact: Carry cannot be greater than 1 for this problem__.
  
* Third problem was related to [Strings](https://leetcode.com/problems/longest-substring-without-repeating-characters/). Longest substring without repeating characters.
  * The simplest solution is to maintain length until a character is repeated, then update max length, drop all characters until the repeated one in substring and start from the next one. Repeat until string is consumed.
  * __Concept: Sliding window -- for range problems in arrays and similar data structures__.
  * The problem with this one was that we reiterated over the characters that are already visited. Definitely there should be a better way. And, there is!
  * The main idea in optimizing this lies in simplicity of the algorithm: if character at index i is repeated the start for next substring is index i+1. Question: What if a character before that is repeated (the hash map will still have it)? Well, that i'+1 is smaller than current i+1. So, always take max with current substring start.
  
* Fourth problem was also related to [Strings](https://leetcode.com/problems/longest-palindromic-substring/). Longest palindromic substring.
  * Well well, this solution was straightforward enough. How do you find out if a string is a palindrome? Simple. You start from middle (or ends) and check if left substring == right substring.
  * So let's see how we can apply that to this problem. Each index i (or i and i+1 together) is the potential center of a palindrome. In order to find the length of the palindrome, start moving out from the center until there's a mismatch between left and right character.
  * Whenever max length is updated, save the palindrome between left and right.
