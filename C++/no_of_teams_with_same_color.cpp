#include <iostream>
#include <vector>
using namespace std;

int main() {
    int  n;
    cin >> n;
    vector <int> home_codes(101,0);
    vector <int> guest_codes(101, 0);

    int home, guest;
    for(int i=0 ; i<n ; ++i){
        scanf("%d %d", &guest, &home);
        home_codes[home]++;
        guest_codes[guest]++;
    }
    
    int count = 0;
    
    for(int i=1 ; i<=100 ; ++i){
        count += home_codes[i] * guest_codes[i];
    }
    cout << count;
    
    return 0;
}
