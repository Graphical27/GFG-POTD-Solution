
from typing import List


class Solution:
    def isPossible(self, n : int, arr : List[int]) -> bool:
        # code here
        dp = [[0]*(n+1) for _ in range(2025)]
        
        for i in range(n+1):
            dp[0][i] = True
            
        for s in range(1, 2025):
            for i in range(n):
                dp[s][i+1] = dp[s][i]
                if s >= arr[i]:
                    dp[s][i+1] = dp[s][i+1] or dp[s-arr[i]][i]
                if dp[s][i+1] and (s%20 == 0 or s%24 == 0 or s == 2024):
                    return True
        
        return False



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
        
        N = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isPossible(N, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends