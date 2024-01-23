#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

using namespace std;

int n, m;
vector<int> fold;
vector<vector<int>> cut;
vector<vector<int>> answer;

int main() {
    n = 8;
    m = 6;
    fold = {1, -1, -1};
    cut = {{1, 1}, {2, 2}, {4, 4}};

    // n = 4;
    // m = 4;
    // fold = {1, 1};
    // cut = {{3, 1}};

    answer.assign(n, vector<int>(m, 1));


    // 겹치는 부분 좌표 (LU 기준)
    //vector<vector<vector<pair<int,int>>>> overlaps(n, vector<pair<int,int>>(m));
    
    map<pair<int,int>, vector<pair<int,int>>> overlap;
    map<pair<int,int>, pair<int,int>> where;

    int fold_n = n;
    int fold_m = m;

    // 접기
    for(int f: fold) {
        // 가로 접기
        if(f == 1) {
            for(int i = 0; i < fold_n; i++) {
                int l = 0;
                int r = fold_m-1;

                while(l < r) {
                    //overlaps[i][l] = make_pair(i, r);
                    pair<int,int> pair_l = make_pair(i, l);
                    pair<int,int> pair_r = make_pair(i, r);

                    if(overlap.find(pair_l) == overlap.end()) {
                        overlap[pair_l] = vector<pair<int,int>>();
                    }
                    if(overlap.find(pair_r) == overlap.end()) {
                        overlap[pair_r] = vector<pair<int,int>>();
                    }

                    overlap[pair_l].push_back(pair_r);
                    overlap[pair_r].push_back(pair_l);

                    where[pair_r] = pair_l;
                    l++;
                    r--;
                }
            }

            fold_m /= 2;
        }

        // 세로 접기
        if(f == -1) {
            for(int j = 0; j < fold_m; j++) {
                int l = 0;
                int r = fold_n-1;

                while(l < r) {
                    pair<int,int> pair_l = make_pair(l, j);
                    pair<int,int> pair_r = make_pair(r, j);

                    if(overlap.find(pair_l) == overlap.end()) {
                        overlap[pair_l] = vector<pair<int,int>>();
                    }
                    if(overlap.find(pair_r) == overlap.end()) {
                        overlap[pair_r] = vector<pair<int,int>>();
                    }

                    overlap[pair_l].push_back(pair_r);
                    overlap[pair_r].push_back(pair_l);

                    where[pair_r] = pair_l;
                    l++;
                    r--;
                }
            }

            fold_n /= 2;
        }

    }


    //모든 map 출력하기
    for (const auto& pair : overlap) {
        std::cout << "Key: (" << pair.first.first << ", " << pair.first.second << "), Value: [";
        for (const auto& element : pair.second) {
            std::cout << "(" << element.first << ", " << element.second << ") ";
        }
        std::cout << "]\n";
    }


    // 자르기
    for(auto c : cut) {
        int ci = --c[0];
        int cj = --c[1];
        cout << ci << cj << "\n";
        pair<int,int> cur_pos = make_pair(ci, cj);


        // 겹친 자를 부분
        vector<pair<int,int>> cut_overlap;
        queue<pair<int, int>> q;
        set<pair<int,int>> visited;
        
        cut_overlap.push_back({ci, cj});
        q.push({ci, cj});
        visited.insert({ci, cj});

        while(!q.empty()) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for(auto p: overlap[{x, y}]) {
                int xx = p.first;
                int yy = p.second;

                if(visited.find({xx, yy}) == visited.end()) {
                    visited.insert({xx, yy});
                    q.push({xx, yy});
                    cut_overlap.push_back({xx, yy});
                }
            }
        }


        // cout << "visited\n" ;
        // for(auto a : visited) {
        //     int i = a.first;
        //     int j = a.second;

        //     cout << i << j << "\n";
        // }

        cout << "overlap \n";

        for(auto a : cut_overlap) {
            int i = a.first;
            int j = a.second;

            cout << i << j << "\n";
        }


        // 겹친 부분 자르기
        for(auto c : cut_overlap) {
            // cout << p.first << " " << p.second << '\n';
            int i = c.first;
            int j = c.second;
            answer[i][j] = 0;
        }

    }



    for(int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << answer[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}