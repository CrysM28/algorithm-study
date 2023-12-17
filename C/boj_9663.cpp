// N-Queen

#include <iostream>
#include <vector>

using namespace std;

int N;
int answer = 0;
int board[15];

bool check(int i, int j) {
    for (int x = i-1; x >= 0; x--) {
        // 세로
        if (board[x] == j)  return false;

        // 대각선
        if (abs(i - x) == abs(j - board[x])) return false;
    }

    return true;
}


void put_queens(int queen) {
    if (queen == N) {
        // for (auto& b: board)
        //     cout << b << " ";
        // cout << "\n";
        answer++;
        return;
    }

    for(int col = 0; col < N; col++) {
        if(check(queen, col)) {
            //cout << "--yes" << queen << col <<  "\n";
            board[queen] = col;
            put_queens(queen + 1);
            board[queen] = -1;
        }
    }
}



int main() {
    cin >> N;

    for (int i = 0; i <= N; i++) {
        board[i] = -1;
    }

    put_queens(0);

    cout << answer;


}