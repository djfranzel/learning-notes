'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

# I started a solution and almost had it. chatGPT created this solution
# same idea, better, more condensed code

class Solution:

    def isHappy(self, n) -> bool:
        seen_numbers = set()
        while n != 1:
            n = sum([int(char) ** 2 for char in str(n)])
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
        return True
                
solution = Solution()
print(solution.isHappy(19))
print(solution.isHappy(2))
print(solution.isHappy(190))
