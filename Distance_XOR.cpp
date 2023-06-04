#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> X(n), Y(n);
    for (int i = 0; i < n; i++)
        cin >> X[i] >> Y[i];
    
map<int, map<int, int>> seen;
int ans = 0;
for (int A=0; A<=k; A++) {
 // For a fixed A (ie x1^x2)
  for (int j=0; j<n; j++) {
    xj = X[j], yj = Y[j];
    xi = A^xj, yi = (k-A)^yj;
    ans += seen[xi][yi];
    seen[xj][yj]++;
  }
}
cout << ans << endl;





}