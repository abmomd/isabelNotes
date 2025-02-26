#include <bits/stdc++.h>
using namespace std;

void sameOccurences()
{
    /*
    Question 1 : Check if all characters have same number of occurences
        */

    string s = "abccbaabccba";

    map<char, int> mp;

    int l = s.size();
    // Gives the length of the String.
    // To access a string character --> Use s[index]

    for (int i = 0; i < l; i++)
    {
        char ch = s[i];
        mp[ch]++;
    }
    cout << endl;

    // How to access the map.

    char ch = s[0]; // First character of the string
    // To find the value of the key in a map. --> mp["key"]
    int occ = mp[ch];
    bool flag = false;
    for (auto i : mp)
    {

        if (i.second != occ)
        {
            flag = true;
            break;
        }
    }

    if (flag == true)
    {
        cout << "Not same occurences";
    }

    else
    {
        cout << "Same No. Of Occurences";
    }
}

void commonAndOneOccurence()
{

    // Question 2 : Count Common Words With Exactly One Occurence

    /*
    1. Create Two maps for individual Arrays.
    2. We will iterate through one array and find common elements (exactly once) in second array.
    */

    vector<string> arr1 = {"leetcode", "is", "amazing", "is", "great"};
    vector<string> arr2 = {"leetcode", "is", "amazing", "great", "great"};

    // map<string,int> mp1;
    // map<string,int> mp2;

    map<string, int> mp1, mp2;

    for (auto i : arr1)
    {
        // string s = i;
        mp1[i]++;
    }

    for (auto i : arr2)
    {
        mp2[i]++;
    }

    for (auto i : mp1)
    {
        cout << i.first << " " << i.second << endl;
    }

    cout << "mp2" << endl;
    for (auto i : mp2)
    {
        cout << i.first << " " << i.second << endl;
    }
    int count = 0;
    for (auto i : mp2)
    {

        // i.first --> Represent the key
        // i.second --> Represents the Value

        string key = i.first;
        int val = i.second;

        if (val != 1)
            continue;
        // We need to check if the key is also present in the second map or not ?
        // And we have to check if it is occuring exactly once or not.

        int val_In_Second_Map = mp1[key];
        if (val_In_Second_Map == 1)
        {
            count++;
        }
    }

    cout << "Count of String with Common and One Occurence is: " << count << endl;
}

int main()
{

    // Define map --> map<DataType1, DataType2> name ;
}
