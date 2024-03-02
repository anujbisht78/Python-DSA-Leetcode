"""
2652 - Sum Multiples

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.

Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.

Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
"""

def sumOfMultiples(self, n: int) -> int:
        sum=0
        i=1
        while i<=n:
            if i%3==0 or i%5==0 or i%7==0:
                sum=sum+i
            i+=1
        return sum
