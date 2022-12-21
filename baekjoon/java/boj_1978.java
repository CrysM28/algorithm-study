package baekjoon.java;

import java.io.*;
import java.util.*;

public class boj_1978 {

    static boolean prime(int x) {
        for (int i = 2; i < (int) Math.sqrt(x) + 1; i++) {
            if (x % i == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        int count = 0;

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num == 1)
                continue;
            if (prime(num)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
