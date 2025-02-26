#include <bits/stdc++.h>
using namespace std;

int main(){

    // Defining Map
    map<int , set<char>> mp;

    string s = "B0B6G0R6R0R6G9G6B5G5R5";
    int n = s.size();
    for(int i=0; i<n; i+=2)
    {
        char ring = s[i];
        int rod = s[i+1] - '0';
        mp[rod].insert(ring);       
    }
    int count = 0;
    for(auto i : mp){
        // cout<<i.first<<endl;
        auto st = i.second;
        if(st.size() == 3) count++;    
    }

    cout<<count<<endl;

}