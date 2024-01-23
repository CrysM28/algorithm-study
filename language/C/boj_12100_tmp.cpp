vector<vector<ll>> left(vector<vector<ll>> board) {
    int cur_num = 0;
    int ptr;

    for(int i = 0; i < N; i++) {


        for(int j = 1; j < N; j++) {
            if (board[i][j] == 0)   continue;

            cur_num = board[i][j];
            ptr = j-1;

            cout << " " << j <<  " " <<  ptr << " " << cur_num << "\n";

            while (ptr >= 0) {
                // 빈칸일 시 이동
                if (board[i][ptr] == 0) {
                    cout << "blank" << "\n";
                    if(ptr == 0) break;
                    ptr--;
                }

                // 같은 숫자면 합침
                else if (board[i][ptr] == cur_num) {
                    cout << "same" << "\n";
                    board[i][ptr] *= 2;
                    board[i][j] = 0;
                    break;
                }

                // 다른 숫자면 멈춤
                else if (board[i][ptr] != cur_num) {
                    cout << "diff" << "\n";
                    ptr++;
                    break;
                }
            }

            cout << ptr <<  " " <<  cur_num << "\n";

            if (board[i][ptr] == 0) {
                board[i][ptr] = cur_num;
                board[i][j] = 0;
            }

            cout << "=== \n";
            for(int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++)
                    cout << board[i][j] << " ";
                cout << "\n";
            }
            cout << "=== \n";
            // cout << "=== \n";
            // for(int i = 0; i < N; i++) {
            //     for (int j = 0; j < N; j++)
            //         cout << board[i][j] << " ";
            //     cout << "\n";
            // }
            // cout << "=== \n";
        }
    }

    return board;
}