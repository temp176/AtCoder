#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++) {
        cin >> A.at(i) >> B.at(i);
    }

    // ここにプログラムを追記
    // (ここで"試合結果の表"の2次元配列を宣言)

    vector<vector<char>> res_table(N, vector<char>(N, '-'));

    for(int i = 0; i < M; i++){
        int a = A.at(i) - 1;
        int b = B.at(i) - 1;

        res_table.at(a).at(b) = 'o';
        res_table.at(b).at(a) = 'x';
    }

    for(vector<char> row: res_table){
        for(int i = 0; i < row.size(); i++){
            if(i == row.size() - 1){
                cout << row.at(i) << endl;
            }
            else cout << row.at(i) << ' ';
        }
    }
}
