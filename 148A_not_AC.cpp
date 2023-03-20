/**

Insomnia cure
«One dragon. Two dragon. Three dragon», — the princess was counting.
She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could.
Tonight she imagined that all dragons were here to steal her, and she was fighting them off.
Every k-th dragon got punched in the face with a frying pan.
Every l-th dragon got his tail shut into the balcony door.
Every m-th dragon got his paws trampled with sharp heels.
Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight,
if the princess counted a total of d dragons?


Solution:
a U b         = a + b - ab
a U b U c     = a + b + c - ab - bc - ca + abc
a U b U c U d = a + b + c + d - ab - bc - cd - da - ac - bd + abc + bcd + cda + dab - abcd

*/


#include <bits/stdc++.h>

#define is_coPrime(x,y) ((x)%2==0 && (y)%2==0)||((x)%3==0 && (y)%3==0)||((x)%5==0 && (y)%5==0)||((x)%7==0 && (y)%7==0)

using namespace std;

int main()
{
    vector<int> arr;
    int num1, num2, num3, num4, n;
    cin>>num1>>num2>>num3>>num4>>n;

    if(is_coPrime(num1, num2) || num1==num2){
        if (num1>num2) num1=-1; else num2=-1;
    }


    if(is_coPrime(num2, num3) || num2==num3){
        if (num2>num3) num2=-1; else num3=-1;
    }


    if(is_coPrime(num3, num4) || num3==num4){
        if (num3>num4) num3=-1; else num4=-1;
    }


    if(is_coPrime(num4, num1) || num4==num1){
        if (num4>num1) num4=-1; else num1=-1;
    }


    if(is_coPrime(num1, num3) || num1==num3){
        if (num1>num3) num1=-1; else num3=-1;
    }


    if(is_coPrime(num2, num4) || num2==num4){
        if (num2>num4) num2=-1; else num4=-1;
    }


    if(num1!=-1) arr.push_back(num1);
    if(num2!=-1) arr.push_back(num2);
    if(num3!=-1) arr.push_back(num3);
    if(num4!=-1) arr.push_back(num4);

    int ans, len = arr.size();

    // cout<<len<<endl;

    if (len==1)
    {
        ans = n/arr[0];
    }
    else if(len==2)
    {
        int a = arr[0], b = arr[1];
        int one_at_a_time = n/a + n/b;
        int two_at_a_time = n/(a*b);
        ans = one_at_a_time - two_at_a_time;
    }
    else if(len==3)
    {
        int a = arr[0], b = arr[1], c = arr[2];
        int one_at_a_time = n/a + n/b + n/c;
        int two_at_a_time = n/(a*b) + n/(b*c) + n/(a*c);
        int three_at_a_time = n/(a*b*c);
        ans = one_at_a_time - two_at_a_time + three_at_a_time;
    }
    else
    {
        int a = arr[0], b = arr[1], c = arr[2], d = arr[3];
        int one_at_a_time = n/a + n/b + n/c +n/d;
        int two_at_a_time = n/(a*b) + n/(b*c) + n/(c*d) + n/(d*a) + n/(a*c) + n/(b*d);
        int three_at_a_time = n/(a*b*c) + n/(b*c*d) + n/(c*d*a) + n/(d*a*b);
        int four_at_a_time = n/(a*b*c*d);
        ans = one_at_a_time - two_at_a_time + three_at_a_time - four_at_a_time;
    }

    cout<<ans;

    return 0;
}