

#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    cout<<"Enter the three number : ";
    cin>>a>>b>>c;
    if(a>b){
        if(a>c){
            cout<<"Maximum number is : "<<a;
        }
        else{
            cout<<"Maximum number is : "<<c;
        }
    }
    else{
        if(b>c){
            cout<<"Maximum number is : "<<b;
        }
        else{
            cout<<"Maximum number is : "<<c;
        }}
    return 0;}


    



