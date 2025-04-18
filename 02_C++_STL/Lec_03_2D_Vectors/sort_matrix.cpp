#include<bits/stdc++.h>
using namespace std;


int main(){

    // Take the input from the user to form a matrix.

    int m,n;
    cin>> m >> n;

    vector<vector<int>> matrix;

    for(int i=0; i <m; i++){
        vector<int> temp;
        for(int j=0;j<n;j++){
                int x;
                cin>>x;
                temp.push_back(x);
        }
        matrix.push_back(temp);
    }

    vector<int> v;

    for(int i=0; i <m; i++){
        for(int j=0;j<n;j++){
            v.push_back(matrix[i][j]);
        }
    
    }
    sort(v.begin(),v.end());
    int index = 0;
    for(int i=0; i <m; i++){
        for(int j=0;j<n;j++){

            matrix[i][j] = v[index];
            index++;

        }
    
    }

    for(int i=0; i <m; i++){
        for(int j=0;j<n;j++){
            cout<<matrix[i][j]<<" ";
        }cout<<endl;
    
    }

}