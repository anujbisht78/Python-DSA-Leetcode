"""
905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
"""

def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]%2==0:
                i+=1
            else:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j-=1

        return nums
