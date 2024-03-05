#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<vector<int>> lines (pow(2,n), vector<int>(n, 0));
    for (long i = 1; i < lines.size(); i++){
        vector<int> line = lines[i];
        for (long ic = 0; ic < line.size(); ic ++){
        }
    }   
    /**for (long i2 = lines.size()/2 + 1; i2 < lines.size(); i2++){
        string outline2 = "";
        vector<int> line2 = lines[i2];
        for (long ic2 = 0; ic2 < line2.size(); ic2 ++){
            line2[ic2] = 1;
            if (ic2 < i2 - n){
                line2[ic2] = 0;
            }
            outline2.append(to_string(line2[ic2]));
        }
        cout << outline2 << endl;
    }**/
}