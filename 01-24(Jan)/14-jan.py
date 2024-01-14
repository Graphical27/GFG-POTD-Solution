#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        array=[]
        index_array=[]
        
        for i in range(m):
            if(arr[i] in array):
                index_array.append(i)
            array.append(arr[i])
        return(index_array)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends