#User function Template for python3

class Solution:
        def antiDiagonalPattern(self,matrix):
            capacity = n**2
            i = 0
            j = 0
            traversed = 0
            res = []
            while traversed < capacity :
                if j==n : 
                    j -= 1
                    i += 1
                tmpi = i
                tmpj = j
                while tmpi >= 0 and tmpj >= 0 and tmpi < n and tmpj <n :
                    res.append(matrix[tmpi][tmpj])
                    traversed += 1
                    tmpi += 1
                    tmpj -= 1
                j += 1
            return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends