
import java.util.Scanner;

public class correct_parentheses {

    public String solution(String s) {
        String answer = "NO";

        int a = 0, b = 0;
        char[] arr = s.toCharArray();
        for (char x : arr) {
            if (x == '(') a++;
            else b++;
        }
        if ((a == b) && (arr[s.length()-1] == ')')) {
            return "YES";
        }

        return answer;
    }

    public static void main(String args[]) {

        correct_parentheses T = new correct_parentheses();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(T.solution(s));
        sc.close();
    }
    
}
