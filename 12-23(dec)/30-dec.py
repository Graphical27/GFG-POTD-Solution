#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
            dic={}
            l=[]
            freq=0
            for i in range(len(arr)):
                if arr[i] not in dic:
                    dic[arr[i]]=1
                else:
                    dic[arr[i]]+=1
                freq=max(freq,dic[arr[i]])
            for i,j in dic.items():
                if j==freq:
                    l.append(i)
            return [min(l),freq]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends