//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
  public:
 vector<vector<int>> sumZeroMatrix(vector<vector<int>> a)
    {
        // Code Here
        int n = a.size(), m = a[0].size();
        int anscol = m, ansrow = n, mxarea = 0, reqheight = -1, reqwidth = -1;
        vector<vector<int>> pre = a;
        
        
        for (int i = 0; i < n; i++)
        {
            for (int j = 1; j < m; j++)
            {
                pre[i][j] += pre[i][j - 1];
            }
        }
        
        
        for (int col = m - 1; col >= 0; col--)
        {
            for (int j = m - 1; j >= col; j--)
            {
                unordered_map<int, int> mp;
                mp[0] = -1;
                int sum = 0;
                int width = j - col + 1;
                for (int row = 0; row < n; row++)
                {
                    sum += pre[row][j] - pre[row][col] + a[row][col];
                    if (mp.find(sum) != mp.end())
                    {
                        int height = row - mp[sum];
                        int area = height * width;
                        if (area > mxarea || (area == mxarea && (col < anscol or (col == anscol && height > reqheight))))
                        {
                            mxarea = area;
                            reqheight = height;
                            reqwidth = width;
                            ansrow = mp[sum] + 1;
                            anscol = col;
                        }
                    }
                    if (!mp.count(sum))
                        mp[sum] = row;
                }
            }
        }
        if (mxarea == 0) return {{}};
        vector<vector<int>> ans(reqheight, vector<int>(reqwidth));
        for (int i = 0; i < reqheight; i++)
        {
            for (int j = 0; j < reqwidth; j++)
            {
                ans[i][j] = a[ansrow + i][j + anscol];
            }
        }

        return ans;
    }
};


//{ Driver Code Starts.




int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        
        vector<vector<int>> a(n,vector<int>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        Solution ob;
        vector<vector<int>> ans = ob.sumZeroMatrix(a);
        if(ans.size() == 0){
            cout<<-1<<endl;
        }
        else{
            for(int i=0;i<ans.size();i++){
                for(int j=0;j<ans[0].size();j++){
                    cout<<ans[i][j]<<" ";
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
// } Driver Code Ends