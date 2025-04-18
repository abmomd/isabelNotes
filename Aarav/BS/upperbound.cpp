#include<bits/stdc++.h>
using namespace std;


int main(){

    int n = 8;
    int arr[8] = {3, 7, 9, 10, 18, 18, 20, 25};
    int key = 20;
    int s = 0;
    int e = 7, ans = -1;

    while (s <= e)
    {
        int mid = (s + e) / 2;


      
        if(arr[mid] > key)
        {   
            ans = mid;

            // TO check for the lower bound on left side.
            e = mid - 1;
        }
        else{
            s = mid + 1;
        }
    }

    cout<<ans<<endl;

}
// smallest index "i" such that arr[i] > key.
//  arr = [1,2,3,4,5,7,9]

// key = 6
// lower_bound = 5