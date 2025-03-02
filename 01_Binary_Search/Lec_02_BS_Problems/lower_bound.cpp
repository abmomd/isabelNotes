#include <bits/stdc++.h>
using namespace std;

void usingLinearSearch(){

        // Using linear Search
    int n = 7;
    int arr[n] = {2, 5, 7, 9, 14, 19, 25};
    int target = 26;

    int ind = -1;

    for (int i = 0; i < 7; i++)
    {

        if (arr[i] >= target)
        {
            ind = i;
            break;
        }
    }

    if (ind == -1)
        cout << n << endl;
    else
        cout << ind << endl;

}

void usingBinarySearch(){

    // Using Binary Search.
    int n = 7;
    int arr[n] = {2, 5, 7, 9, 14, 19, 25};
    int target = 20;

    int l = 0, r = n-1, ans = n;

    while(l <= r){
        
        int mid = (l+r)/2;

        if(arr[mid] >= target){
            ans = mid;
            r = mid - 1;
        }
        else{
            l = mid+1;
        }

    }

    cout<<ans<<endl;

}

int main()
{

    // Direct Function which helps us to calculate the lower bound.
    int n = 7;
    vector<int> arr = {2,5,9,14,22,25,29};
    int target = 5;

    int ans = lower_bound(arr.begin(), arr.end(), target) - arr.begin();

    cout<< ans <<endl;


}