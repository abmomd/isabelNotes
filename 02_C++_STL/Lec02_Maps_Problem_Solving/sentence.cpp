#include<bits/stdc++.h>
using namespace std;

int main(){


    string s = "Extract all words from this sentence";
    // Output should be ["Extract" , "all", "words", "from","this","sentence"]

    // Adding a single space in the string s.
    // s += ' ';

    string currWord="";
    vector<string> ans;
    // for(int i =0; i<s.size();i++){
    //     //Access the element like this s[i]
    // }

    for(auto i : s){
        // Access the element like this i
        
        if(i == ' '){
            
            ans.push_back(currWord);
            currWord="";


        }else{
            currWord += i;
        }


    }

    ans.push_back(currWord);

    for(auto i : ans){
        cout<<i<<endl;
    }


    if(2) cout<<"It worked"<<endl;


}