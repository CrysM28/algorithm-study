#include <iostream>
#include <vector>

#define MIN(a, b) a < b ? a : b

using namespace std;
typedef long long ll;

int N;
vector<pair<ll, ll>> ingrid;

int used[10];
int selected;
//vector<int> selected;

ll answer = int(1e9);
ll sour = 1, bitter;


void make_food(int idx) {
    // 값 계산
    if (selected != 0) {
        ll cur_food = abs(sour - bitter);
        answer = min(answer, cur_food);
        //cout << selected << " " << cur_food << "\n";
    }

    // 재료 다 썼으면 그만
    if (selected == N)   return;

    // 다음 재료 추가
    for(int i = idx; i < N; i++) {
        if (!used[i]) {
            ll s = ingrid[i].first;
            ll b = ingrid[i].second;

            sour *= s;
            bitter += b;
            used[i] = true;
            selected += 1;

            //cout << "sour " << sour << " bit " << bitter << "\n";


            make_food(i);

            sour /= s;
            bitter -= b;
            used[i] = false;
            selected -= 1;

        }
    }


}


int main(void) {
    cin >> N;

    ll s, b;
    for(int i = 0; i < N; i++)  {
        cin >> s >> b;
        ingrid.push_back(make_pair(s, b));
    }

    make_food(0);

    cout << answer;

    return 0;
}