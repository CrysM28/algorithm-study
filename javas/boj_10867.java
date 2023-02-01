package java;

import java.io.*;
import java.util.*;

public class boj_10867 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        List<Integer> nums = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            nums.add(in.nextInt());
        }
        in.close();

        Set<Integer> set = new HashSet<>(nums);
        Integer[] array = set.toArray(new Integer[0]);

        Arrays.sort(array);
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}

