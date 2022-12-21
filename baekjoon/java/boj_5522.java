package baekjoon.java;

import java.io.*;

public class boj_5522 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = 0;
        for(int i=0; i<5; i++) {
            int score = Integer.parseInt(br.readLine());
            total += score;
        }

        System.out.println(total);
    }
}
