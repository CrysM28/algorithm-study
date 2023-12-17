#include <iostream>
#include <vector>

using namespace std;

int N, S;
vector<int> seq;
int answer;


void get_sum(int cur_sum, int idx) {
    if (idx == N) {
        return;
    }

    cur_sum += seq[idx];

    if (cur_sum == S) {
        cout << idx << "\n";
        answer++;
    }

    get_sum(cur_sum, idx+1);

}



int main(void) {
    cin >> N >> S;
    
    int num;
    for(int i = 0; i < N; i++) {
        cin >> num;
        seq.push_back(num);
    }

    for(int i = 0; i < N; i ++) {
        cout << "==" << i << "\n";
        get_sum(0, i);
    }

    cout << answer;

    return 0;
}