#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> sub1 = {1,2,3};
    vector<int> sub2 = {4,5,6,7};
    vector<int> sub3 = {8};

    vector<vector<int>> result;

    result.push_back(sub1);
    result.push_back(sub2);
    result.push_back(sub3);

    result[2][0] = 10;
    // Accessing a specific element
    cout<<"The result is: "<<result[2][0]<<endl;

    int n = result.size();

    for(int i = 0; i<n; i++){

        int m = result[i].size();

        for(int j =0; j<m; j++){
            cout<<result[i][j]<<" ";
        }cout<<endl;


    }
    // Using auto
    for(auto i : result){
        // i --> is a vector

        for(auto j : i){
            cout<<j<<" ";
        }cout<<"\n";
    }



}