#include <bits/stdc++.h>
using namespace std;

char repeatedCharacter(string s)
{
    map<char, int> mp;
    for (auto i : s)
    {
        if (mp[i] == 1)
        {
            return i;
        }
        else
        {
            mp[i] = 1;
        }
    }

    return 'a';
}

int main()
{

    char ans = repeatedCharacter("abccab");
    cout << "First Letter to appear twice is: " << ans << endl;
}