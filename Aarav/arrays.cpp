#include <bits/stdc++.h>
using namespace std;

int main()
{

    // Declare an Arrays
    int arr[5];

    // Initialize the arrays
    int arr1[3] = {5, 9, 15};

    // Initialize an array with all elements as 0.
    int n = 10;
    int arr2[10] = {0};

    for (int i = 0; i < n; i++)
    {
        cout << arr2[i] << " ";
    }
    cout<<endl;
    // Vectorss

    // vector<data type> name;

    vector<int> v = {1,2,3,4};

    v.push_back(5);
    v.push_back(15);

    v.pop_back();

    v.push_back(50);
    v.push_back(25);

    for(int i=0; i<7; i++){
        cout<<v[i]<<" ";
    }

}