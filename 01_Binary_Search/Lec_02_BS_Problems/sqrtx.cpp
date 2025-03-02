#include<bits/stdc++.h>
using namespace std;

void usingLinearSearch(){

    long long  x;
    cin>>x;
    int ans;
    for(long long  i=1; i<x; i++){
        long long val = i * i;

        if(val <= x){
            ans = i;
        }
        else{
            break;
        }
    }

    cout<<ans<<endl;

}

int main(){


    long long target;
    cin>>target;

    int left =1, right = target, ans = -1;

    while(left <= right){

        int mid = ( left + right)/ 2;

        long long val = mid * mid;

        if(val <= target){
            ans = mid;
            left = mid + 1;
        }
        else{
            right = mid-1;
        }

    }

    cout<<"The sqrt is: "<<ans<<endl;




}