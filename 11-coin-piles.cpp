#include <iostream>
using namespace std;
int main (){
    int t;
    cin >> t;
    while(t--){
        int a,b;
        cin >> a >> b;
        if (a < b) swap(a , b); //learned i can just do this instead of using minmax
        if (b == 0 && a != 0){
            cout << "NO" << endl; //filtering 0,0 cases
        }
        else if (a > 2*b){
            cout << "NO" << endl; //there is no hope, even with only -1 hits to b
        }
        else {
            a %= 3; //-3 to each after alternating moves ..
            b %= 3; //.. remaining |a-b| is the key metric
            if (a < b) swap (a, b);
            if((a == 0 && b == 0) || (a == 2 && b == 1)){
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }
    } 
    return 0;
}