#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin>>n;

    int arr[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }


    for(int i=0; i<n; i++){

        if(i%2==0){
            for(int j=0; j<n; j++){
                cout<<arr[i][j]<<" ";
            }
        }
        else{
            for(int j=n-1; j>=0; j--){
                cout<<arr[i][j]<<" ";
            }
        }
    }

}

// 10 20 30 40 ---> 45 35 25 15 --->100 200 300 400 ---> 450 350 250 150