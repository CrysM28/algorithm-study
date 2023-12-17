#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>

#define MAX 101

using namespace std;

int N, M;
// vector<vector<int>> grid;

int grid[MAX][MAX];
bool visited[MAX][MAX];
int dist[MAX][MAX];

int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

queue<pair<int,int>> q;

void BFS() {
    q.push(make_pair(1, 1));
    dist[1][1]++;

    while(!q.empty()) {
        int i = q.front().first;
        int j = q.front().second;

        q.pop();

        if (i == N && j == M)
            return;

        for (int x=0; x < 4; x++) {
            int ni = i + di[x];
            int nj = j + dj[x];

            if (ni > 0 && ni <= N && nj > 0 && nj <= M && grid[ni][nj] == 1) {
                grid[ni][nj] = 2;
                dist[ni][nj] = dist[i][j] + 1;
                q.push(make_pair(ni, nj));
            }
        }
    }
}




int main() {
    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        string row;
        cin >> row;
        
        for (int j = 1; j <= M; j++) {
            grid[i][j] = row[j-1]-'0';
        }
    }

    // for (int i = 0; i <= N; i++) {
    //     for (int j = 0; j <= M; j++) {
    //         cout << grid[i][j];
    //     }
    //     cout << "\n";
    // }


    BFS();
    cout << dist[N][M];


    // for(int i = 0; i <= N; i++) {
    //     for(int j = 0; j <=M; j++) {
    //         cout << dist[i][j];
    //     }
    //     cout << '\n';
    // }


    return 0;
}