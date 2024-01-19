#User function Template for python3

from collections import defaultdict

class Solution:
    def kTop(self,a, N, K):
        count = defaultdict(int)
        count.clear()
        ans = []
        for ai in a:
            count[ai]+=1
            k = list(count.keys())
            k.sort(key=lambda x: (-count[x], x))
            i = k.index(0) if 0 in k else N
            ans.append(k[:min(K,i)])
        return ans
#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends