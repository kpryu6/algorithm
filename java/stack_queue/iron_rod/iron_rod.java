import java.util.*;

public class iron_rod {

    public int solution(String s) {
        int answer= 0;

        Stack<Character> stack = new Stack<>();
        char[] arr = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if (arr[i] == '(') stack.push(arr[i]);
            else {
                // Àü¿¡²¨ '(' ÀÌ¸é
                if (arr[i-1] == '(') {
                    stack.pop();
                    answer += stack.size();
                }
                else {
                    stack.pop();
                    answer += 1;
                }
                
            }
        }
        return answer;
    }

    public static void main(String args[]) {

        iron_rod T = new iron_rod();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(T.solution(s));
        sc.close();
    }
    
}
 