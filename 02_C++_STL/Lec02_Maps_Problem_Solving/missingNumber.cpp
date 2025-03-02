#include <bits/stdc++.h>
using namespace std;

int missingNumber(vector<int> &nums)
{
    map<int, int> mp;
    int n = nums.size();
    for (auto i : nums)
    {
        mp[i] = 1;
        // It will create a key = i and give the value as 1.
    }
    int ans = -1;
    for (int i = 0; i <= n; i++)
    {
        if (mp[i] != 1)
        {
            ans = i;
        }
    }

    return ans;
}

int main()
{

    vector<int> nums = {0, 1, 3};
    int ans = missingNumber(nums);
    cout << "Missing Number is: " << ans << endl;
}