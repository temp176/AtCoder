#include <bits/stdc++.h>
using namespace std;


int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> BA;
    for(int i = 0; i < N; i++){
        int a, b;
        cin >> a >> b;
        BA.push_back(make_pair(b, a));
    }

    sort(BA.begin(), BA.end());

    for(pair<int, int> ba: BA){
        cout << ba.second << ' ' << ba.first << endl;
    }
}
