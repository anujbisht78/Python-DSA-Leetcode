"""
1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
"""

def findLucky(self, arr: List[int]) -> int:
        count=0
        ans=[]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    count+=1
            if arr[i]==count:
                ans.append(count)
            count=0    


        if len(ans)>0:
            return max(ans)
        else:
            return -1