
import java.util.*;

public class remove_parentheses {

    public String solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (char x : s.toCharArray()) {
            if (x == ')') {
                // '(' 전까지 제거
                while (stack.peek() != '(') {
                    if (!stack.isEmpty()) stack.pop();
                }
                // '(' 제거
                if (!stack.isEmpty()) stack.pop();
            }
            else stack.push(x);
        }

        return stack.stream().collect(StringBuilder::new, StringBuilder::append, StringBuilder::append).toString();
    }

    public static void main(String args[]){
        remove_parentheses T = new remove_parentheses();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(T.solution(s));
        sc.close();
    }

}
// stream()
// 컬렉션(Collection)과 배열(Array) 등의 데이터 소스를 다루는데 유용한 API이며 스트림은 각각의 원소를 순차적으로 처리하며, 병렬 처리도 가능하다.

// collect()
// 스트림의 각 원소를 하나의 결과 컨테이너에 수집하는 최종 연산이다.
// 이 때 결과 컨테이너는 Supplier, Accumulator, Combiner 세 가지 인터페이스를 구현한 객체로 정의됩니다.