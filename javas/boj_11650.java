package java;

import java.io.*;
import java.util.*;

public class boj_11650 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[][] coor = new int[N][2];

        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            coor[i][0] = Integer.parseInt(st.nextToken());
            coor[i][1] = Integer.parseInt(st.nextToken());
        }

        Comparator<int[]> comparator = new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                int r = a[0] - b[0];
                if(r==0) r = a[1] - b[1];
                return r;
            }
        };
        
        Arrays.sort(coor, comparator);

        for(int i=0; i<N; i++) {
            sb.append(coor[i][0]).append(" ").append(coor[i][1]).append("\n");
        }

        System.out.println(sb);

    }
}
