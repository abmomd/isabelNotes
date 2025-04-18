#include<iostream>
using namespace std;

void checkEven(int n){
    if(n%2 == 0){
        cout<<"Even";
    }
    else{
        cout<<"Odd";
    }
}

void checkDigit(){
    int n;
    cin>>n;

    int sum = 0;
    while(n > 0){
        int rem = n%10;
        cout<<rem<<endl;
        n = n/10;
        sum = sum + rem;
    }
    cout<<"Sum is: "<<sum<<endl;

}

int main(){

    int a,b,c;
    cin>>a>>b>>c;

    cout<<a<<" "<<b<<" "<<c<<endl;

    // We will use max function to find it.
    int maxNum = max(a,max(b,c));
    int minNum = min(a,(min(b,c)));

    cout<<maxNum - minNum<<endl;


}