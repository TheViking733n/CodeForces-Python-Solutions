/**

Epic Game
Simon and Antisimon play a game.
Initially each player receives one fixed positive integer that doesn't change throughout the game.
Simon receives number a and Antisimon receives number b. They also have a heap of n stones.
The players take turns to make a move and Simon starts.
During a move a player should take from the heap the number of stones equal to the greatest common divisor
of the fixed number he has received and the number of stones left in the heap.
A player loses when he cannot take the required number of stones
(i. e. the heap has strictly less stones left than one needs to take).

*/

#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    if (b==0) return a;
    if (a%b==0) return b;
    return gcd(b, a%b);
}

int main()
{
    int n, a, b;
    cin>>a>>b>>n;
    while(n>0)
    {
        // Simon's move
        n -= gcd(n,a);
        if(n==0){
            cout<<0;
            break;
        }

        // Antisimon's move
        n -= gcd(n,b);
        if(n==0){
            cout<<1;
            break;
        }
    }
    return 0;
}