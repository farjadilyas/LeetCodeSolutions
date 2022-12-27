/*
  268. Missing Number
  [ Medium ] | [ ?% ] -- Solved 25/12/2022

  Problem:
  - Given two integers a and b, return the sum of the two integers without using the operators + and -.

  APPROACH:
  - Use Java to get around Python's handling of negative integers and their binary representation :P
  - Given two numbers
    - bitwise XOR -> the answer we would get if we ignored the carry over values
    - bitwise AND -> the per-binary-digit carry over values
    - explanation: The answer, ignoring the carry over values, will only show a 1 when an XOR of the two inputs would
    - similarly, we only get carry over values when BOTH input digits are ones, which is why we use the AND operator to
      get the carry over values
  - Since isolating a single binary digit at a time using mod 2 is probably slow..
  - Another approach is to get the answer without carry overs added, get the carry over itself, and apply the same logic
    again until the carry over values are 0

  Time Complexity: O(1) - Since the numbers are limited to 32 bits, that's a hard upper bound on how many iterations
    can occur due to the carry over not settling to 0
  Space Complexity: O(1)
*/


class Solution {
    public int getSum(int a, int b) {
        int carry = 1;
        int inter = 0;
        while (carry != 0) {
            inter = a^b;
            carry = (a&b)<<1;
            a = inter;
            b = carry;
        }
        return inter;
    }
}