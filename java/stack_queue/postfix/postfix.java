
import java.util.*;

public class postfix{

    public int solution(String s){
        int answer=0;

        Stack<Integer> stack = new Stack<>();

        for (char x : s.toCharArray()){
            if (Character.isDigit(x)){
                stack.push(Character.getNumericValue(x));
            }
            else if (x == '+'){
                int num2 = stack.pop();
                int num1 = stack.pop();
                answer = num1 + num2;
                stack.push(answer);
            }
            else if (x == '-'){
                int num2 = stack.pop();
                int num1 = stack.pop();
                answer = num1 - num2;
                stack.push(answer);
            }
            else if (x == '*'){
                int num2 = stack.pop();
                int num1 = stack.pop();
                answer = num1 * num2;
                stack.push(answer);
            }
            else if (x == '/'){
                int num2 = stack.pop();
                int num1 = stack.pop();
                answer = num1 / num2;
                stack.push(answer);
            }
        }
           
        

        return answer;
    }

    public static void main(String args[]){

        postfix T = new postfix();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.println(T.solution(s));
        sc.close();
    }
}

