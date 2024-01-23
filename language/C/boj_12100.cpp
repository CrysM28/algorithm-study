#include <iostream>
#include <vector>

#define MAX(a, b) a>b ? a : b

using namespace std;
typedef long long ll;

int N;
int answer;


vector<vector<ll>> left(vector<vector<ll>> board) {
    int cur_num;
    int ptr;

    for(int i = 0; i < N; i++) {
        ptr = 0;
        for(int j = 1; j < N; j++) {
            if (board[i][j] == 0)   continue;

            cur_num = board[i][j];
            board[i][j] = 0;

            // 빈칸일 시 그 칸으로 이동
            if (board[i][ptr] == 0) {
                board[i][ptr] = cur_num;
            }

            // 같은 숫자면 합치고 그 칸 완료
            else if (board[i][ptr] == cur_num) {
                board[i][ptr] *= 2;
                ptr++;
            }

            // 다른 숫자면 다음 칸부터
            else {
                ptr++;
                board[i][ptr] = cur_num;
            }
        }
    }

    return board;
}

vector<vector<ll>> right(vector<vector<ll>> board) {
    int cur_num;
    int ptr;

    for(int i = 0; i < N; i++) {
        ptr = N-1;
        for(int j = N-2; j >= 0; j--) {
            if (board[i][j] == 0)   continue;

            cur_num = board[i][j];
            board[i][j] = 0;

            // 빈칸일 시 그 칸으로 이동
            if (board[i][ptr] == 0) {
                board[i][ptr] = cur_num;
            }

            // 같은 숫자면 합치고 그 칸 완료
            else if (board[i][ptr] == cur_num) {
                board[i][ptr] *= 2;
                ptr--;
            }

            // 다른 숫자면 다음 칸부터
            else {
                ptr--;
                board[i][ptr] = cur_num;
            }
        }
    }

    return board;
}

vector<vector<ll>> down(vector<vector<ll>> board) {
    int cur_num;
    int ptr;

    for(int j = 0; j < N; j++) {
        ptr = N-1;
        for(int i = N-2; i >= 0; i--) {
            if (board[i][j] == 0)   continue;

            cur_num = board[i][j];
            board[i][j] = 0;

            // 빈칸일 시 그 칸으로 이동
            if (board[ptr][j] == 0) {
                board[ptr][j] = cur_num;
            }

            // 같은 숫자면 합치고 그 칸 완료
            else if (board[ptr][j] == cur_num) {
                board[ptr][j] *= 2;
                ptr--;
            }

            // 다른 숫자면 다음 칸부터
            else {
                ptr--;
                board[ptr][j] = cur_num;
            }
        }
    }

    return board;
}

vector<vector<ll>> up(vector<vector<ll>> board) {
    int cur_num;
    int ptr;

    for(int j = 0; j < N; j++) {
        ptr = 0;
        for(int i = 1; i < N; i++) {
            if (board[i][j] == 0)   continue;

            cur_num = board[i][j];
            board[i][j] = 0;

            // 빈칸일 시 그 칸으로 이동
            if (board[ptr][j] == 0) {
                board[ptr][j] = cur_num;
            }

            // 같은 숫자면 합치고 그 칸 완료
            else if (board[ptr][j] == cur_num) {
                board[ptr][j] *= 2;
                ptr++;
            }

            // 다른 숫자면 다음 칸부터
            else {
                ptr++;
                board[ptr][j] = cur_num;
            }
        }
    }

    return board;
}

int get_max(vector<vector<ll>> board) {
    int cur_max = 0;

    for(int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cur_max = MAX(cur_max, board[i][j]);
        }
    }

    return cur_max;
}



void play(int move, vector<vector<ll>> board) {
    if (move == 5) {
        answer = max(answer, get_max(board));

        // cout << "=== \n"; 
        // for(int i = 0; i < N; i++) {
        //     for (int j = 0; j < N; j++)
        //         cout << board[i][j] << " ";
        //     cout << "\n";
        // }
        // cout << "=== \n";
        return;
    }
    
    play(move+1, left(board));
    play(move+1, right(board));
    play(move+1, up(board));
    play(move+1, down(board));


}




int main() {
    cin >> N;

    vector<vector<ll>> board(N, vector<ll>(N));

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    play(0, board);
    cout << answer;

    return 0;
}