"""
2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 
Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
"""

def countPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i,v in enumerate(nums):
            if v in d:
                d[v].append(i)
            else:
                d|={v:[i]}
        s=0
        def make(a,n):
            c=0
            for i in range(n-1):
                for j in range(i+1,n):
                    if a[i]*a[j]%k==0:
                        c+=1
            return c
        for i in d:
            if len(d[i])==1:
                continue
            s+=make(d[i],len(d[i]))
        return s