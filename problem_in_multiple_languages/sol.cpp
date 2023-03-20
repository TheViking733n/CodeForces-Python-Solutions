// Programmer: The Viking
// Date: 19.08.2022


#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, x;
    cout << "Enter size of array: ";
    cin >> n;
    map<int, pair<int, int>> freq;    // freq and ind
    vector<pair<pair<int, int>, int>> nums;
    cout << "Enter array: ";
    for (int i = 0; i < n; i++) {
        cin >> x;
        freq[x].first++;
        if (freq[x].first == 1) {
            freq[x].second = i;
        }
    }
    for (auto it : freq) {
        nums.push_back(make_pair(make_pair(-it.second.first,it.second.second), it.first));
    }
    sort(nums.begin(), nums.end());

    for (auto it : nums) {
        cout << it.second << " ";
    }
    return 0;

}