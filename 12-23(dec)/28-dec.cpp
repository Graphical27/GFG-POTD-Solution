//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++
class Solution{
    public:
    vector<vector<int>> dp;
    bool func(int i, int j, string &wild, string &pattern, int m,int  n){
        if(i==m && j==n){
            return true;
        }
        if(i==m || j==n){
            return false;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        if(wild[i]==pattern[j]){
            return dp[i][j] = func(i+1, j+1, wild, pattern, m, n);
        }
        if(wild[i]=='?'){
            return dp[i][j] = func(i+1, j+1, wild, pattern, m, n);
        }
        if(wild[i]=='*'){
            int k=j;
            while(k<=n){
                bool t = func(i+1, k, wild, pattern, m, n);
                if(t){
                    return dp[i][j] = true;
                }
                k++;
            }
        }
        return dp[i][j] = false;
    }
    bool match(string wild, string pattern)
    {
        // code here
        int m = wild.length();
        int n = pattern.length();
        dp.resize(m+1, vector<int>(n+1, -1));
        return func(0, 0, wild, pattern, m, n);
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t-->0)
    {
        string wild, pattern;
        cin>>wild>>pattern;
        
        Solution ob;
        bool x=ob.match(wild, pattern);
        if(x)
        cout<<"Yes\n";
        else
        cout<<"No\n";
    }
    return 0;
}
// } Driver Code Ends