// # I have an sorted array of n elements, I want to find the total number of duplicates  of a key element in the array.

// Ex: [1,1,2,2,2,2,3,3,3,3,4,5,6,7,8,9,10]
// key = 2
// ans = 4

#include <bits/stdc++.h>
using namespace std;

int main()
{

    vector<int> v = {3, 6, 8, 11, 16, 19};

    int arr[6] = {3, 6, 8, 11, 16, 19};

    int key = 16;
    //  For Vectors
    if (binary_search(v.begin(), v.end(), key))
    {
        cout << "Key Found" << endl;
    }
    else
    {
        cout << "Key Not Found" << endl;
    }



    // For Arrays

    if(binary_search(arr, arr + 6, key))
    {
        cout << "Key Found" << endl;
    }
    else
    {
        cout << "Key Not Found" << endl;
    }


    // Lower Bound in C++ STL
    //  For finding the actual element in the array
    int val = *lower_bound(v.begin(), v.end(), key);
    cout << "Lower Bound: " << val << endl;

    // Find the index of the lower bound
    int index = lower_bound(v.begin(), v.end(), key) - v.begin();
    cout << "Index of Lower Bound: " << index << endl;


    //Upper Bound in C++ STL
    int val1 = *upper_bound(v.begin(), v.end(), key);
    cout << "Upper Bound: " << val1 << endl;

    // Find the index of the upper bound
    int index1 = upper_bound(v.begin(), v.end(), key) - v.begin();
    cout << "Index of Upper Bound: " << index1 << endl;
}