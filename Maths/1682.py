"""
1862 - Sum of Floored Pairs

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.
The floor() function returns the integer part of the division.

Example 1:

Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.

Example 2:

Input: nums = [7,7,7,7,7,7,7]
Output: 49
"""

def sumOfFlooredPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxVal = max(nums)
        cache = [0 for i in range(maxVal + 1)]
        for key in freq:
            num = freq[key]
            count = 1
            while count*key <= maxVal:
                cache[count*key] += num
                count += 1
        
        count = 0
        result = 0
        for i in range(len(cache)):
            count += cache[i]
            if i in freq:
                result += freq[i] * count
        
        return result % (10**9 + 7)