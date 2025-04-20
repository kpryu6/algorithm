
import java.util.*;

public class remove_parentheses_inflearn {

    public String solution(String s) {
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for (char x : s.toCharArray()) {
            if (x == ')') {
                // ¸ÕÀú ²¨³¿
                while (stack.pop()!= '(');
            }
            else stack.push(x);
        }

        for (int i = 0; i < stack.size(); i++) {
            answer += stack.get(i);
        }

        return answer;
    }

    public static void main(String args[]){
        remove_parentheses_inflearn T = new remove_parentheses_inflearn();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(T.solution(s));
        sc.close();
    }

}