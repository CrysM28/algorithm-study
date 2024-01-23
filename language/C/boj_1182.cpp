#include <iostream>
#include <vector>

using namespace std;

int N, S;
vector<int> seq;
int answer;

vector<int> indices;
bool used[21];
int cur_sum = 0;

void get_sum(int start_idx) {
    if (cur_sum == S && !indices.empty()) {
        // for(auto& a: indices)
        //     cout << a << " ";
        // cout << "\n";
        answer += 1;
    }

    if (indices.size() == N) {
        return;
    }

    for(int i = start_idx; i < N; i++) {
        if(!used[i]) {
            indices.push_back(i);
            used[i] = true;
            cur_sum += seq[i];
            get_sum(i);
            indices.pop_back();
            used[i] = false;
            cur_sum -= seq[i];

        }
    }

}



int main(void) {
    cin >> N >> S;
    
    int num;
    for(int i = 0; i < N; i++) {
        cin >> num;
        seq.push_back(num);
    }

    get_sum(0);

    cout << answer;

    return 0;
}