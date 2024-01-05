//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    int sumOfPowers(int a, int b){
    int ans = 0;
    for (int num=a;num<=b;num++){
        int x = num; 
        if(x==1) continue;
        for(int i=2;i*i<=x;i++){
            while(x%i==0){
                x/=i;
                ans++;
            }
        }
        if(x!=1) ans++;
    }
    return ans;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int a, b;
		cin >>  a >> b;
		Solution obj;
		int ans = obj.sumOfPowers(a, b);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends