#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int t=0;
    cin >> t;

    while(t--){
        int n=0;
        cin >> n;

        int arr[n];

        for(int i=0;i<n;i++){
            cin >> arr[i];
        }

        if(n==1){
            cout<<"YES"<<"\n";
            continue;
        }

        sort(arr,arr+n);
        bool a = true;
        for(int i=1;i<n;i++){
            if(arr[i]-arr[i-1] >1 || arr[i]-arr[i-1]<-1){
                cout<<"NO"<<"\n";
                a=false;
                break;
            }
        }

        if(a){
            cout<<"YES"<<"\n";
        }
    }
}