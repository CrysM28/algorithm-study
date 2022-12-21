package baekjoon.java;

import java.io.*;

public class boj_2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String ascend = "1 2 3 4 5 6 7 8";
        String descend = "8 7 6 5 4 3 2 1";

        if(input.equals(ascend))
            System.out.println("ascending");
        else if(input.equals(descend))
            System.out.println("descending");
        else
            System.out.println("mixed");
    }
}
