
// 굳이 노드를 만들 필요가 없었는걸?

import java.util.*;
public class find_calf_inflearn {

    int answer = 0;
    int[] dis = {-1, 1, 5};
    int[] ch;
    Queue<Integer> Q = new LinkedList<>();

    public int BFS(int start, int end) {

        ch = new int[10001];
        ch[start] = 1;
        Q.offer(start);
        int L = 0;

        while(!Q.isEmpty()) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                int cur = Q.poll();
                // if (cur == end) return L;
                for (int x : dis) {
                    int n = cur+x;
                    // x레벨 이니 하나 더 +
                    if (n == end) return L+1;
                    if (n >= 1 && n <= 10000 && ch[n] == 0) {
                        ch[n] = 1;
                        Q.offer(n);
                    }
                }
            }
            L++;
        }
        return 0;


    }

    public static void main(String args[]) {

        find_calf_inflearn T = new find_calf_inflearn();
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        System.out.println(T.BFS(start, end));
        sc.close();

    }
    
}
