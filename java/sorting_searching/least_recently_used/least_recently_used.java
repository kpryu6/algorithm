import java.util.*;

public class least_recently_used {

    public Queue<Integer> solution(int cacheSize, int workOut, int[] workOutArr) {

        Queue<Integer> Q = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < workOut; i++) {
            // 메모리에 존재하면
            if (Q.contains(workOutArr[i])) {
                Q.remove(workOutArr[i]);
                Q.offer(workOutArr[i]);
            }
            else Q.offer(workOutArr[i]);

            // 사이즈 초과 시
            if (Q.size() > cacheSize) Q.poll();
        }
        // stack을 이용한 Q 뒤집기
        while (!Q.isEmpty()) stack.push(Q.poll());
        while (!stack.isEmpty()) Q.offer(stack.pop());

        return Q;
    }

    public static void main(String args[]) {

        least_recently_used T = new least_recently_used();
        Scanner sc = new Scanner(System.in);
        int cacheSize = sc.nextInt();
        int workOut = sc.nextInt();
        int[] workOutArr = new int [workOut];

        for (int i = 0; i < workOut; i++) {
            workOutArr[i] = sc.nextInt();
        }

        for (Integer x : T.solution(cacheSize, workOut, workOutArr)) {
            System.out.print(x + " ");
        }
        sc.close();
    }
    
}
