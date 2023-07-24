# Subarray with given sum

"""Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4

"""
def subArraySum(self,arr, n, s): 
        i = 0
        curr = 0
        if s == 0:
            return [-1]                                                      
        for j in range(n):
            curr += arr[j]
            while curr > s:
                curr -= arr[i]
                i += 1
            if curr == s:
                return i + 1, j + 1
        return [-1]

