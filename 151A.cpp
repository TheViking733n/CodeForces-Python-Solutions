/**
Soft Drinking

This winter is so cold in Nvodsk! A group of n friends decided to buy k bottles of a soft drink called
"Take-It-Light" to warm up a bit. Each bottle has l milliliters of the drink.
Also they bought c limes and cut each of them into d slices. After that they found p grams of salt.

To make a toast, each friend needs nl milliliters of the drink, a slice of lime and np grams of salt.
The friends want to make as many toasts as they can, provided they all drink the same amount.
How many toasts can each friend make?




Solution:

k bottles
l milliliters
c limes
d slices
p grams of salt

n, k, l, c, d, p, nl, np
3  4  5  10 8 100  3  1


toasts = k*l / nl

limes = c*d

salts = p/np

ans = min(toasts, limes, salts)/n
 */




#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k, l, c, d, p, nl, np;
    cin>>n>>k>>l>>c>>d>>p>>nl>>np;

    int toasts = k*l / nl;
    int limes = c*d;
    int salts = p/np;
    int ans = min(min(toasts, limes), salts)/n;

    cout<<ans;

    return 0;
}
