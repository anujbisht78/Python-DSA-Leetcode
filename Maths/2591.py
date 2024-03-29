"""
2591 - Distribute Money to Maximum Children

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:
1. All money must be distributed.
2. Everyone must receive at least 1 dollar.
3. Nobody receives 4 dollars.

Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

Example 1:

Input: money = 20, children = 3
Output: 1
Explanation: 
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

Example 2:

Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.
"""

def distMoney(self, money: int, children: int) -> int:

        if money < children: return -1 
        ans = 0 
        for j in range(1,children+1):
            leftmoney = money - 8       # if current child gets 8$
            leftchildren = children - j
            if leftmoney >= leftchildren: 
                money = leftmoney 
                ans += 1 
            else: 
                leftchildren = children - j + 1   # 1 is added because current child
                                                  #  has not gotten any dollar yet
                if leftchildren == 1 and money == 4:
                    ans -= 1
                money = 0
                break
        if money > 0:       # if some money is left to distribute
            ans -= 1
        return ans