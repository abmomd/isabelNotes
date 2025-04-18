#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n = 8;
    int arr[8] = {3, 7, 9, 10, 15, 18, 20, 25};
    int key = 18;
    int s = 0;
    int e = 7, ans = -1;

    while (s <= e)
    {
        int mid = (s + e) / 2;

        if (key == arr[mid])
        {
            ans = mid;
            break;
        }
        else if (key > arr[mid])
        {
            s = mid + 1;
        }
        else
        {
            e = mid - 1;
        }
    }

    if (ans == -1)
    {
        cout << "Not Found" << endl;
    }
    else
    {
        cout << "Element Found: " << arr[ans] << endl;
    }
}