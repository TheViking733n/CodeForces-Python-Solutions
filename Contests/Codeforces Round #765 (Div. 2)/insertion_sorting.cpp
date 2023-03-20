// C++ program to implement insertion sort using STL.
#include <bits/stdc++.h>

using namespace std;

// Function to sort the array
void insertionSort(vector<int> &vec)
{
    for (auto it = vec.begin(); it != vec.end(); it++)
    {        
        // Searching the upper bound, i.e., first 
        // element greater than *it from beginning
        auto const insertion_point = 
                upper_bound(vec.begin(), it, *it);
          
        // Shifting the unsorted part
        rotate(insertion_point, it, it+1);        
    }
}
  
// Function to print the array
void print(vector<int> vec)
{
    for( int x : vec)
        cout << x << " ";
    cout << '\n';
}
  
// Driver code
int main()
{
    vector<int> arr = {2, 1, 5, 3, 7, 5, 4, 6};    
    insertionSort(arr);    
    print(arr);
}