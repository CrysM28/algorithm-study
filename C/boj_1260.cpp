
// DFS / BFS

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define NL "\n"

using namespace std;

int N, M, start;
vector<vector<int>> v;

bool DFS_visited[1001];
bool BFS_visited[1001];
vector<int> DFS_result;
vector<int> BFS_result;


void DFS(int node) {
    if (!DFS_visited[node]) {
        DFS_result.push_back(node);
        DFS_visited[node] = true;
        for (int i = 0; i < v[node].size(); i++)
            DFS(v[node][i]);
    }
}

void BFS() {
    queue<int> q;

    BFS_result.push_back(start);
    q.push(start);
    BFS_visited[start] = true;

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        for (int i = 0; i < v[x].size(); i++) {
            if (!BFS_visited[v[x][i]]) {
                BFS_result.push_back(v[x][i]);
                BFS_visited[v[x][i]] = true;
                q.push(v[x][i]);
            }
        }
    }
}


int main() {

    cin >> N >> M >> start;
    v.assign(N+1, vector<int>());

    for (int i = 0; i < M; i++) {
        int s, e;
        cin >> s >> e;

        v[s].push_back(e);
        v[e].push_back(s);
    }

    for (int i = 1; i <= N; i++) {
        sort(v[i].begin(), v[i].end());
    }

    DFS(start);
    BFS();

    for (auto r: DFS_result) {
        cout << r << ' ';
    }

    cout << NL;

    for (auto r: BFS_result) {
        cout << r << ' ';
    }

    return 0;
}