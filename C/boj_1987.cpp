#include <iostream>
#include <vector>

#define MAX(a,b) a > b ? a : b

using namespace std;

int R, C;
vector<vector<char>> board(20, vector<char>(20, ' '));
bool visited[27];
int answer = 1;


void DFS(int i, int j, int move) {
    // 종료 조건 체크
    if (i < 0 || i >= R || j < 0 || j >= C) return;

    int alpha = board[i][j] - 'A';   
    if(visited[alpha])  return;

    // cout << "i " << i <<" j "<< j << " " << board[i][j] << " " << alpha << "\n";
    // cout << "move " << move << "\n"; 

    // 갱신
    answer = max(answer, move);

    // DFS + backtrack
    visited[alpha] = true;
    DFS(i+1, j, move+1);
    visited[alpha] = false;

    visited[alpha] = true;
    DFS(i-1, j, move+1);
    visited[alpha] = false;

    visited[alpha] = true;
    DFS(i, j+1, move+1);
    visited[alpha] = false;

    visited[alpha] = true;
    DFS(i, j-1, move+1);
    visited[alpha] = false;


}



int main() {
    cin >> R >> C;

    string input;
    for(int i = 0; i < R; i++) {
        cin >> input;
        for(int j = 0; j < C; j++) {
            board[i][j] = input[j];
        }
    }

    DFS(0, 0, 0);

    int a = 'A' - 'A';
    int b = 'Z' - 'A';
    cout << a << " " << b << "\n";

    cout << answer;


    // for(int i = 0; i < R; i++) {
    //     for(int j = 0; j < C; j++) {
    //         cout << board[i][j];
    //     }
    //     cout << "\n";
    // }

    return 0;
}