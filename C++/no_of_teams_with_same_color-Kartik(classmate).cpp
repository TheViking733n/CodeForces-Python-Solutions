#include <iostream>
 
using namespace std;
 
typedef struct pairteam {
    int home;
    int guest;
};
 
int main() {
    int n;
    cin>>n;
    pairteam pairs[n];
    for(int i = 0; i < n; ++i) {
        cin>>pairs[i].home>>pairs[i].guest;
    }
    int count = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if (pairs[i].guest == pairs[j].home) {
                ++count;
            }
        }
    }
    cout<<count;
    return 0;
}
