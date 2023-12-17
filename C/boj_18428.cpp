#include <iostream>
#include <vector>

using namespace std;

int N;
vector<vector<char>> grid(6, vector<char>(6,' '));

vector<pair<int,int>> s_pos;    // 학생 좌표
vector<pair<int,int>> x_pos;    // 빈칸 좌표
int x_size;

vector<int> o_idx;  // 빈칸 중 장애물 놓을 위치 idx
bool used[40];

bool can_hide;


// put obstacle
vector<vector<char>> get_new_grid(vector<vector<char>> grid) {
    int i, j;

    for(int x = 0; x < 3; x++) {
        i = x_pos[o_idx[x]].first;
        j = x_pos[o_idx[x]].second;
        grid[i][j] = 'O';
    }

    return grid;
}


// do search
bool find_student(vector<vector<char>> grid) {
    int i, j;
    bool is_found = false;

    for(auto p: s_pos) {
        i = p.first;
        j = p.second;

        // L
        for(int nj = j-1; nj >= 0; nj--) {
            if (grid[i][nj] == 'T') return true;
            else if (grid[i][nj] == 'O')    break;
        }

        // R
        for(int nj = j+1; nj < N; nj++) {
            if (grid[i][nj] == 'T') return true;
            else if (grid[i][nj] == 'O')    break;
        }

        // U
        for(int ni = i-1; ni >= 0; ni--) {
            if (grid[ni][j] == 'T') return true;
            else if (grid[ni][j] == 'O')    break;
        }

        // D
        for(int ni = i+1; ni < N; ni++) {
            if (grid[ni][j] == 'T') return true;
            else if (grid[ni][j] == 'O')    break;
        }
    }

    return false;

}


void play(int idx) {
    if (can_hide)   return;

    if (o_idx.size() == 3) {
        // for(auto a: o_idx)  cout << a << " ";
        // cout << "\n";

        bool is_found = find_student(get_new_grid(grid));        
        if (!is_found)  can_hide = true;
        return;
    }

    for (int i = idx; i < x_size; i++) {
        if (!used[i]) {
            used[i] = true;
            o_idx.push_back(i);
            play(i);
            used[i] = false;
            o_idx.pop_back();

        }
    }
}



int main() {
    cin >> N;

    char input;

    for(int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> input; 

            grid[i][j] = input;

            if(input == 'X')
                x_pos.push_back(make_pair(i, j));
            else if(input == 'S')
                s_pos.push_back(make_pair(i, j));
        }
    }

    x_size = x_pos.size();

    play(0);

    if(can_hide)
        cout << "YES";
    else
        cout << "NO";


    // for(auto a: blank_pos){
    //     cout << a.first << " " << a.second;
    //     cout << "\n";
    // }

    // for(int i = 0; i < N; i++) {
    //     for (int j = 0; j < N; j++) {
    //         cout << grid[i][j];
    //     }
    //     cout << "\n";
    // }


    return 0;
}