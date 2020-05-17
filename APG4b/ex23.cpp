#include <bits/stdc++.h>
using namespace std;


int main() {
    int N;
    cin >> N;

    map<int, int> counter;

    for(int i = 0; i < N; i++){
        int a;
        cin >> a;

        if(counter.count(a)) counter[a]++;
        else counter[a] = 1;
    }

    int res_key = -1;
    int res_value = -1;
    for(pair<int, int> c: counter){
        int key = c.first;
        int value = c.second;

        if(res_value < value){
            res_value = value;
            res_key = key;
        }
    }

    cout << res_key << ' ' << res_value << endl;
}
