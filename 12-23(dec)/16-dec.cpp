#include<bits/stdc++.h>
using namespace std;
long long int countStr(long long int n);

int main(){
    int t;
    cin >>t;
    while (t--)
    {
        long long int n;
        cin>>n;
        cout<< countStr(n) << endl;
    }
    return 0;
}

long long int countStr(long long int n){
    return (pow(n,3)+3*n+2)/2;
}
