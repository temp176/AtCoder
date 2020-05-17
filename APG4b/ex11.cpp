#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A;
    cin >> N >> A;

    int res = A;

    for(int i = 0; i < N; i++){
        string op;
        int B;
        cin >> op >> B;
        if(op == "+"){
            res += B;
        }
        else if(op == "-"){
            res -= B;
        }
        else if(op == "*"){
            res *= B;
        }
        else if(op == "/"){
            if(B == 0) {
                cout << "error" << endl;
                break;
            }
            res /= B;
        }

        cout << i + 1 << ":" << res << endl;
    }
}
