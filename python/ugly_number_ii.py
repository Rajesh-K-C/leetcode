# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
# Constraints:
# 1 <= n <= 1690

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [None]*n
        result[0] = 1
        p2=0
        p3=0
        p5=0
        for i in range(1,n):
            result[i] = min(result[p2]*2, result[p3]*3, result[p5]*5)
            if result[i] == result[p2]*2:
                p2 += 1
            if result[i] == result[p3]*3:
                p3 += 1
            if result[i] == result[p5]*5:
                p5 += 1
        return result[n-1]