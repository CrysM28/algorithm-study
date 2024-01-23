
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class 폰켓몬 {
    public static void main(String[] args) throws IOException {
        폰켓몬 sol = new 폰켓몬();
        int[] input = {3,1,2,3};
        int result = sol.solution(input);
        System.out.println(result);
    }

    public int solution(int[] nums) {
        int select = nums.length / 2;
        
        Set<Integer> uniqueNums = new HashSet<>();
        for (int num : nums) {
            uniqueNums.add(num);
        }
        int noRepeat = uniqueNums.size();
        
        if (select < noRepeat) {
            return select;
        } else {
            return noRepeat;
        }
    }
}
