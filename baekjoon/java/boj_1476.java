package baekjoon.java;
import java.io.*;
import java.util.StringTokenizer;

public class boj_1476 {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputs = br.readLine();
        StringTokenizer st = new StringTokenizer(inputs);
        int E = Integer.parseInt(st.nextToken()); 
        int S = Integer.parseInt(st.nextToken()); 
        int M = Integer.parseInt(st.nextToken()); 

        int year = 0;

        while(true){
            int x = year % 15;
            int y = year % 28;
            int z = year % 19;
            if (x == E-1 && y == S-1 && z == M-1){
                break;
            }
            year++;
        }

        bw.write(year+1+"");
        bw.flush();
        bw.close();

	}

}
