#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    int res = 1;

    for(int i = 1; i < S.size() - 1; i++){
        if(S.at(i) == '+') res += 1;
        else if(S.at(i) == '-') res -= 1;
    }

    cout << res << endl;
}
