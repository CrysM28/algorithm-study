package baekjoon.java;

import java.io.*;
import java.util.*;

public class boj_15486 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N+1];

        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            int price = Integer.parseInt(st.nextToken());

            dp[i+1] = Math.max(dp[i], dp[i+1]);
            if(i+time <= N)
                dp[i+time] = Math.max(dp[i+time], dp[i] + price);
        }

        bw.write(dp[N] + "\n");
        bw.flush();
        bw.close();
    }
}
