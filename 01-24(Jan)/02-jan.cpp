//{ Driver Code Starts
// C++ program to find largest subarray sum with
// at-least k elements in it.
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:    
     long long int maxSumWithK(long long int nums[], long long int n, long long int k) {
        vector<long long int>dp(n,0);
        long long int currSum=0;
        for(int i=0; i<n; i++){
            currSum+=nums[i];
            dp[i]=max(dp[i],currSum);
            if(currSum<=0) currSum=0;
        }
        long long int ans=0;
        currSum=0;
        for(int i=0; i<k; i++) currSum+=nums[i];
        int i=0,j=k;
        ans=currSum;
        while(j<n){
            currSum=currSum+nums[j]-nums[i];
            i++;
            ans=max(ans,currSum+dp[i-1]);
            j++;
        }
        return ans;
    }
};

//{ Driver Code Starts.

// Driver code
int main() {
    long long int t;
    cin >> t;
    while (t--) {
        long long int n, k, i;
        cin >> n;
        long long int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        cin >> k;
        Solution ob;
        cout << ob.maxSumWithK(a, n, k) << endl;
    }
    return 0;
}

// } Driver Code Ends