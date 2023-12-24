
#User function Template for python3

class Solution:
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        if n == 1:
            return matrix[0][0]
        trans = list(zip(*matrix[1:]))
        return sum(((-1)**i) * matrix[0][i] * self.determinantOfMatrix(trans[:i]+trans[i+1:], n-1) for i in range(n))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends