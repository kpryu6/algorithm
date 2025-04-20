import java.util.*;

public class rescue_princess {

    public int solution (int n, int k) {

        Queue<Integer> Q = new LinkedList<>();
        // 먼저 넣어주고
        for (int i = 1; i <= n; i++) Q.offer(i);

        while(!Q.isEmpty()) {
            // k-1 까지 빼주고 뒤로 넣기
            for (int i = 1; i < k; i++) Q.offer(Q.poll());
            // k번째꺼 빼기
            Q.poll();
            // 하나 남았으면 그게 답임
            if (Q.size() == 1) break;
        }

        return Q.poll();
    }

    public static void main(String args[]){

        rescue_princess T = new rescue_princess();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        System.out.println(T.solution(n,k));
        sc.close();
    }
    
}
