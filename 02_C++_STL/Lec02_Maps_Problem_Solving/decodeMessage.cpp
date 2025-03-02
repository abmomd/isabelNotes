#include <bits/stdc++.h>
using namespace std;

string decodeMessage(string key, string message)
{
    map<char, char> mp;
    char ch = 'a';
    for (auto i : key)
    {

        if (i == ' ')
            continue;
        else if (mp[i])
            continue;
        else
            mp[i] = ch;
        ch++;
    }

    // for (auto i : mp)
    // {
    //     cout << i.first << " " << i.second << endl;
    // }

    for (int i = 0; i < message.length(); i++)
    {
        if (message[i] == ' ')
            continue;
        message[i] = mp[message[i]];
    }
    return message;
}

int main()
{

    string ans = decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv");
    cout << ans << endl;
}
