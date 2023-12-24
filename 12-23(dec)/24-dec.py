

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        ans = 0
        for i, x in sorted(enumerate(price), key=lambda a: a[1]):
            buy = min(k // x, i + 1)
            if buy == 0:
                break
            ans += buy
            k -= buy * x
        return ans



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends