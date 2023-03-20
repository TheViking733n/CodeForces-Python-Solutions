/**

Next Round

"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round,
as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores.
Calculate how many participants will advance to the next round.




n-> no. of participants
*/


#include <iostream>

using namespace std;

int main()
{
    int n, k, a, count=0, k_th_score=-1;

    cin>>n>>k;
    for(int i=1 ; i<=n ; ++i)
    {
        cin>>a;
        if(a>0)
        {
            if (i<k)
                count++;

            else if(i==k)
            {
                count++;
                k_th_score=a;
            }
            else
            {
                if(k_th_score==a)
                    count++;
                else if (k_th_score>a)
                    break;
            }
        }
        else
            break;
    }
    cout<<count;
    return 0;
}