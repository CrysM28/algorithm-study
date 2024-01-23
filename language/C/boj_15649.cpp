#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> result;
bool check[9];

void backtrack() {
    if (result.size() == M) {
        for(int i = 0; i < M; i++)
            cout << result[i] << " ";
        cout << "\n";
        return;
    }

    for(int i=1; i <= N; i++) {
        if (!check[i]) {
            check[i] = true;
            result.push_back(i);
            backtrack();
            result.pop_back();
            check[i] = false;
        }
    }

}


int main() {
    cin >> N >> M;

    backtrack();

    return 0;
}