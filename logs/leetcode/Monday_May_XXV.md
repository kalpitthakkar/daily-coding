## [Monday] May 25, 2020

* First problem was related to understanding of looping and string manipulation. [Zigzag conversion](https://leetcode.com/problems/zigzag-conversion/).
  * The main idea was to have two parts of the string: one is vertical and second is angled.
  * Vertical string comes from top to bottom and angled goes from bottom to top. However, angled does not cover the bottom and top rows.
  * Hence, number of characters in each vertical part is numRows and in each angled part is numRows - 2.
  * This was simple. The tricky part was coding this: the zigzag pattern was nothing more than traversing an array on indices forth and back and forth.
  * The edge case: when there is only 1 row. Problematic. However, I got the hang of it finally.
  
* Second problem was easy. [Reverse an integer](https://leetcode.com/problems/reverse-integer/).
  * This was really easy. The only part to remember is that they gave the lower bound and upper bound to check for overflow.
  * In real world, those bounds won't be given.
  * Simple mod 10 and div 10 operations. Multiply current num by 10 and then add remainder. Original number becomes the quotient.
  * Remember sign initially.
