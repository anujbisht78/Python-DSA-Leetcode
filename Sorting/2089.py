"""
2089. Find Target Indices After Sorting Array

You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
"""

def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l,h=0,len(nums)-1
        left=right=-1
        while l<=h: #For finding the leftmost index of the target element
            m=(l+h)>>1
            if nums[m]==target:
                left=m
                h=m-1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        l,h=left,len(nums)-1
        while l<=h: #For finding the rightmost index of the target element
            m=(l+h)>>1
            if nums[m]==target:
                right=m
                l=m+1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        if left==-1:
            return []
        ans=range(left,right+1)
        return ans         