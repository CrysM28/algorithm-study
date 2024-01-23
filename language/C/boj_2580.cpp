#include <iostream>
#include <vector>

using namespace std;

int board[9][9];
vector<pair<int,int>> blanks;
int blanks_len;

bool found;


bool check(int i, int j, int num) {
    // 세로
    for (int r = 0; r < 9; r++) {
        if (r == i) continue;
        if (board[r][j] == num) return false;
    }

    // 가로
    for (int c = 0; c < 9; c++) {
        if (c == j) continue;
        if (board[i][c] == num) return false;
    }

    // 3x3
    int ii = (i /3) * 3;
    int jj = (j /3) * 3;

    for (int r = ii; r < ii+3; r++) {
        for (int c = jj; c < jj+3; c++) {
            if (board[r][c] == num) return false;
        }
    }

    return true;
}



void fill(int cnt) {
    if (found)  return;

    if (cnt == blanks_len) {
        found = true;
        //cout << "found \n";

        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++)
                cout << board[i][j];
            cout << "\n";
        }

        return;
    }

    int i = blanks[cnt].first;
    int j = blanks[cnt].second;

    for (int num = 1; num <= 9; num++) {
        if (check(i, j, num)) {
            board[i][j] = num;
            fill(cnt+1);
            board[i][j] = 0;
        }
    }

}


int main() {
    int num;

    for (int i = 0; i < 9; i++) {
        string row;
        cin >> row;

        for(int j = 0; j < 9; j++) {
            num = row[j] - '0';
            board[i][j] = num;
            if(num == 0) {
                blanks.push_back(make_pair(i, j));
            }
        }
    }

    blanks_len = blanks.size();



    fill(0);





    // for(auto& i: blanks){
    //     cout << i.first << i.second << "\n";
    // }

    // for(int i = 0; i < 9; i++) {
    //     for(int j = 0; j < 9; j++)
    //         cout << board[i][j] << " ";
    //     cout << "\n";
    // }

    return 0;
}