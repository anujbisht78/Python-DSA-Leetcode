"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
"""

def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            s=0
            e=len(grid[0])-1
            ch=False
            while s<=e:
                mid=(s+e)//2
                if i[mid]<0:
                    ch=True
                    e=mid-1
                else:
                    s=mid+1
            if ch:
                count+=(len(i)-s)       
        return count


