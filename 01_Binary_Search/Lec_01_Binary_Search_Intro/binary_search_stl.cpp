#include <bits/stdc++.h>
using namespace std;

int main()
{

    // User to give an input array in an ascending order.

    int n, key;
    cin >> n >> key;
    // Taking the input for number of elements in array

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    /*
    Approach:
    1. Find the mid element.
    2. Check if the mid element is greater or lesser or equal to the key.
    3. If (mid > key) r = mid-1
    4. if (mid < key ) l = mid + 1
    5. if(mid = key) store and break

    */

    // C++ STANDARD TEMPLATE LIBRARY

    // Only Check if Element is present in the array

    if (binary_search(arr, arr + n, key))
    {
        cout << "Element is Present";
    }
    else
    {
        cout<<"Not Present";
    }

    
}