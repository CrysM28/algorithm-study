package javas;

import java.util.Scanner;

// ChatGPT Python->Java
public class boj_1780 {
    private static final int DIV = 3;

    public static void divide(int n, int i, int j, int[][] paper, int[] ans) {
        int color = paper[i][j];
        for (int x = i; x < i+n; x++) {
            for (int y = j; y < j+n; y++) {
                if (color != paper[x][y]) {
                    for (int ni = i; ni < i+n; ni += n/DIV) {
                        for (int nj = j; nj < j+n; nj += n/DIV) {
                            divide(n/DIV, ni, nj, paper, ans);
                        }
                    }
                    return;
                }
            }
        }

        int idx = color + 1;
        ans[idx]++;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] paper = new int[N][N];
        int[] ans = new int[DIV];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                paper[i][j] = sc.nextInt();
            }
        }

        divide(N, 0, 0, paper, ans);
        for (int i = 0; i < DIV; i++) {
            System.out.println(ans[i]);
        }
    }
}