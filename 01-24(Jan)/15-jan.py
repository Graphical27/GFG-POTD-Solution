
from typing import List
import math
class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        def f(i,n,total,cost,dp):
            if i==n or total<=0:
                return 0
            if dp[i][total]!=-1:
                return dp[i][total]
            pick = 0
            if cost[i]<=total:
                pick = 1+ f(i+1,n,math.floor(total-(10/100*cost[i])),cost,dp)
            not_pick = f(i+1,n,total,cost,dp)
            dp[i][total]= max(pick,not_pick)
            return dp[i][total]

        dp = [[-1] * (total + 1) for _ in range(n + 1)]
        
        return f(0,n,total,cost,dp)

#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends