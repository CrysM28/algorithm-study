package java;

import java.io.*;

public class boj_8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < n; i++) {
            String input = br.readLine().trim();
            int consec = 0;
            int score = 0;

            for (int k = 0; k < input.length(); k++) {
                if (input.charAt(k) == 'O') {
                    consec++;
                    score += consec;
                } else {
                    consec = 0;
                }
            }
            System.out.println(score);
        }
    }

}
