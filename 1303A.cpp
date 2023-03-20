#include <iostream>

using namespace std;

int main()
{
    unsigned int t, left, right, count;
    string binary;

    cin >> t;

    while (t--)
    {
        cin >> binary;
        count = 0;
        if (binary.size() <=2)
            cout<<0<<"\n";

        else
        {
            left = binary.find('1', 0);

            if (left == -1)
            {
                cout<<0<<"\n";
                continue;
            }
            
            
            right = binary.size()-1;

            for (unsigned int i=binary.size()-1; i>=left; i--){
                if (binary[i]=='1'){
                    right = i;
                    break;
                }
            }

            // cout <<left<<" "<<right<<"\n";

            for (unsigned int i=left+1; i<right; ++i){
                if (binary[i]=='0'){
                    ++count;
                }
            }

            cout<<count<<"\n";

        }
    }



    return 0;
}