// ChatGPT로 Python -> Java 변환한 코드

package javas;

import java.util.Scanner;
import java.util.ArrayList;

public class boj_2166 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> x = new ArrayList<>();
        ArrayList<Integer> y = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            x.add(a);
            y.add(b);
        }

        x.add(x.get(0));
        y.add(y.get(0));

        double ans = 0;
        for (int i = 0; i < N; i++) {
            ans += (x.get(i) * y.get(i + 1)) - (x.get(i + 1) * y.get(i));
        }

        System.out.println(String.format("%.1f", Math.abs(ans) / 2));
    }
}


