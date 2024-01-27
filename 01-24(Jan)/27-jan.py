#User function Template for python3
import math
class Solution:
    def matrixChainOrder(self, p, n):
        inf = math.inf
        cost = [[inf for _ in range(n)] for _ in range(n)]
        brac = [['' for _ in range(n)] for _ in range(n)]

        for i in range(n - 1):
            cost[i][i + 1] = 0
            brac[i][i + 1] = chr(ord('A') + i)

        for i in range(2, n):
            for j in range(n - i):
                x = i + j
                for k in range(j + 1, n):  # Fix: range(j+1, n)
                    if cost[j][x] > cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]:
                        cost[j][x] = cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]
                        brac[j][x] = '(' + brac[j][k] + brac[k][x] + ')'

        return brac[0][n - 1]

#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends