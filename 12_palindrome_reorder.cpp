#include <iostream>
#include <string>
using namespace std;
template<class C, typename T>
bool contains(C&& c, T e) { return find(begin(c), end(c), e) != end(c); };
int main(){
    string n;
    char members[] = {};
    int membSize = 0;
    int membfreq[] = {};
    int membfreqsize = 0;
    string output;
    cin >> n;
    int len = n.size();
    // 1. take inventory of frequency of each alphabet
    for (char i : n){
       if (!contains(members, i)){
        members[membSize] = i;
        membSize += 1;
       } 
       membfreqsize = membSize;
       int cx = 0;
       for (char c1 : members){
        for (char c2 : n){
            if (c1 == c2){
                membfreq[cx]++;
            }
        }
        cx += 1;
       }
 
    }
    // 2. filter1 - if len is even & freq of any alphabet is odd then NO SOLUTION, otherwise arrange using i,-i index style in output
    if (len % 2 == 0){

    }
    // 3. filter2 - if len is odd & freq of more/less than one alphabet is odd then NO SOLUTION, otherwise 
    

    return 0;
}