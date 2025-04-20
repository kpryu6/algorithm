

import java.util.*;

public class path_finding_adjacency_list_practice {

    static int n,m,answer=0;
    static int[] ch;
    static ArrayList<ArrayList<Integer>> graph;
    public void DFS(int v) {

        if (v == n) answer++;
        else {
            for (int dtn : graph.get(v)) {
                if (ch[dtn] == 0) {
                    ch[dtn] = 1;
                    DFS(dtn);
                    ch[dtn] = 0;
                }
            }
        }
    }

    public static void main(String args[]) {

        path_finding_adjacency_list_practice T = new path_finding_adjacency_list_practice();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // 정의 먼저 해주고
        graph = new ArrayList<ArrayList<Integer>>();

        // 각 정점의 ArrayList 생성
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 입력값 넣기
        // 1 5 면 1번 ArrayList에 5번 추가
        for (int i = 0; i < m; i++) {
            graph.get(sc.nextInt()).add(sc.nextInt());
        }

        ch = new int[n+1];

        ch[1] = 1;
        T.DFS(1);
        System.out.println(answer);
        sc.close();
        
    }
}
