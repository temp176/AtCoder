#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> point_list(N);
    int point_average = 0;

    for(int i = 0; i < N; i++){
        cin >> point_list.at(i);
        point_average += point_list.at(i);
    }

    point_average /= N;

    for(int i = 0; i < N; i++){
        cout << abs(point_list.at(i) - point_average) << endl;
    }
}
