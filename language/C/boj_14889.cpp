#include <iostream>
#include <vector>

using namespace std;

int N, M;
bool check[20];
int synergy[20][20];

vector<int> team1;
vector<int> team2;

int answer = int(1e9);


void make_team(int idx) {
    if (team1.size() == N/2) {
        // for(auto& i: team1) 
        //     cout << i;
        // cout << "\n";
        
        // make team 2
        team2.clear();
        for(int i = 0; i < N; i++) {
            if (!check[i])  team2.push_back(i);
        }

        // calculate
        int team1_power = 0;
        int team2_power = 0;
        int power_diff = 0;

        for(int i = 0; i < N/2; i++) {
            for (int j = i+1; j < N/2; j++) {
                team1_power += synergy[team1[i]][team1[j]] + synergy[team1[j]][team1[i]];
                team2_power += synergy[team2[i]][team2[j]] + synergy[team2[j]][team2[i]];
            }
        }

        if (team1_power > team2_power)
            power_diff = team1_power - team2_power;
        else
            power_diff = team2_power - team1_power;
        
        if (power_diff < answer) {
            answer = power_diff;
        }

        // for(auto& i: team1) 
        //     cout << i;
        // cout << "\n";
        // cout << team1_power << "\n";
        // cout << team2_power << "\n";
        // cout << power_diff << "\n";


        return;
    }


    for(int i = idx; i < N; i++) {
        if (!check[i]) {
            team1.push_back(i);
            check[i] = true;
            make_team(i+1);
            team1.pop_back();
            check[i] = false;
        }
    }

}



int main() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> synergy[i][j];
        }
    }

    make_team(0);
    
    cout << answer;

    cout << endl;

    return 0;
}