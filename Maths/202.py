"""
202 - Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
1. tarting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
"""

def isHappy(self, n: int) -> bool:
        n=str(n)
        ch=False
        if n=='1':
            ch=True
        else:
            while n not in ('2', '3', '4', '5', '6', '8','9'):
                print(n,1)
                s=0
                for i in n:
                    s+=int(i)**2
                if s==1:
                    ch=True
                    break
                else:
                    n=str(s)
        return ch