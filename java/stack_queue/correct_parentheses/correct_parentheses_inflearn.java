
import java.util.*;

public class correct_parentheses_inflearn {

    public String solution(String s) {
        String answer = "YES";

        Stack<Character> stack = new Stack<>();

        for (char x : s.toCharArray()) {

            if (x == '(') stack.push(x);
            else {
                if (!stack.isEmpty()) stack.pop();
                // stack이 비어있는데 ')'가 아직 있는 경우
                else return "NO";
            }
        }
        // stack에 아직 있는데 s가 끝난 경우
        if (!stack.isEmpty()) return "NO";


        return answer;
    }

    public static void main(String args[]) {

        correct_parentheses_inflearn T = new correct_parentheses_inflearn();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(T.solution(s));
        sc.close();
    }
    
}
