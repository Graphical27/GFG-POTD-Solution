//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Item{
    int value;
    int weight;
};


// } Driver Code Ends
//class implemented
/*
struct Item{
    int value;
    int weight;
};
*/


class Solution{
    public:
    double fractionalKnapsack(int W, Item arr[], int n){
        sort(arr, arr+n, [](Item a, Item b){
            double v1=(double)a.value/a.weight;
            double v2=(double)b.value/b.weight;
            return v1>v2;
        });
        double res=0;
        for(int i=0; i<n; i++){
            int value=arr[i].value;
            int weight=arr[i].weight;
            
            if(!W) break;
            if(W<weight){
                res+=(((double)value/weight)*W);
                break;
            }
            res+=value;
            W-=weight;
        }
        return res;
    }     
};


//{ Driver Code Starts.
int main()
{
	int t;
	//taking testcases
	cin>>t;
	cout<<setprecision(6)<<fixed;
	while(t--){
	    //size of array and weight
		int n, W;
		cin>>n>>W;
		
		Item arr[n];
		//value and weight of each item
		for(int i=0;i<n;i++){
			cin>>arr[i].value>>arr[i].weight;
		}
		
		//function call
		Solution ob;
		cout<<ob.fractionalKnapsack(W, arr, n)<<endl;
	}
    return 0;
}
// } Driver Code Ends