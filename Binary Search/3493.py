"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]

        for i in nums1:
            s=0
            e=len(nums2)-1
            while s<=e:
                mid=(s+e)//2
                if nums2[mid]==i:
                    if nums2[mid] not in ans:
                        ans.append(nums2[mid])
                    break
                elif i<nums2[mid]:
                    e=mid-1
                else:
                    s=mid+1
        return ans