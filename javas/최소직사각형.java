package java;

import java.util.*;

public class 최소직사각형 {
    class Solution {
        public int solution(int[][] sizes) {
            List<Integer> width = new ArrayList<Integer>();
            List<Integer> height = new ArrayList<Integer>(); 

            for(int[] size: sizes) {
                width.add(Math.max(size[0], size[1]));
                height.add(Math.min(size[0], size[1]));
            }

            int answer = Collections.max(width) * Collections.max(height);
            return answer;
        }
    }
}
