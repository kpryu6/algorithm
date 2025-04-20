package stack_queue.curriculum;

import java.util.*;

public class curriculum {

    public String solution (String s, String schedule) {
        String answer = "NO";

        Queue<Character> Q = new LinkedList<>();
        for (char x : s.toCharArray()) {
            Q.offer(x);
        }
        for (char x : schedule.toCharArray()) {
            if (Q.contains(x) && Q.peek() == x) Q.poll();
        }
        if (Q.isEmpty()) answer = "YES";
        return answer;
    }

    public static void main(String args[]){

        curriculum T = new curriculum();
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String schedule = sc.next();
        System.out.println(T.solution(s,schedule));
        sc.close();
    }
    
}
