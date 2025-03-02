#include <bits/stdc++.h>
using namespace std;

void usingLinearSearch()
{

    int n = 9;
    int arr[n] = {1, 2, 2, 2, 6, 6, 6, 9, 10};
    int target = 2;
    int first = -1, last = -1;

    for (int i = 0; i < 9; i++)
    {

        if (first != -1 and arr[i] == target)
        {
            last = i;
        }
        else if (arr[i] == target)
        {
            first = i;
            last = i;
        }
    }

    cout << first << " " << last << endl;
}

int main()
{

    // Using Binary Search.

    vector<int> arr = {1, 3, 6,10};

    int target = 10;

    int first = lower_bound(arr.begin(), arr.end(), target) - arr.begin();
    int last = upper_bound(arr.begin(), arr.end(), target) - arr.begin();

    cout << first << " " << (last - 1 )<< endl;
}