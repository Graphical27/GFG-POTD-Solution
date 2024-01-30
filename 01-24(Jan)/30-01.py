#User function Template for python3

class Solution:

    def helper(self,i,j,k,arr1,arr2,arr3,dp):
        if i < 0 or j < 0 or k < 0:
            return 0
            
        if dp[i][j][k] != -1:
            return dp[i][j][k]
            
        if arr1[i] == arr2[j] and arr2[j]== arr3[k]:
            dp[i][j][k]= 1+self.helper(i-1,j-1,k-1,arr1,arr2,arr3,dp)
            
        else:
            dp[i][j][k]= max(self.helper(i-1,j,k,arr1,arr2,arr3,dp),self.helper(i,j-1,k,arr1,arr2,arr3,dp),self.helper(i,j,k-1,arr1,arr2,arr3,dp))
            
        return dp[i][j][k]    
            

    def LCSof3(self,A,B,C,n1,n2,n3):
        
        dp=[[[-1]*n3 for _ in range(n2)] for _ in range(n1)]
        
        return self.helper(n1-1,n2-1,n3-1,A,B,C,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends