#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
        def atoi(self,s):
        # Code here
            s = s.upper()
            if s[-1]=='-':
                return -1
            ans = 0
            for i in range(65,90+1):
                if chr(i) in s:
                    ans=True
            
            ff = s
            if ans!=True:
                ff=int(s)
            return -1 if ans==True else ff


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends