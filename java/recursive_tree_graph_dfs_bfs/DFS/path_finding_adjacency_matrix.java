// 정점 많아질수록 비효율적

// 한번 방문한 노드는 다시 방문하면 안됨
import java.util.*;
public class path_finding_adjacency_matrix {

    static int answer = 0;
    // check 배열
    static int[] ch;
    // 정점 1~n
    static int n;
    static int[][] graph;

    // 백트래킹하면서 ch[v] = 0으로 만들어야됨..
    public void DFS(int v) {

        if (v == n) answer++;
        else {
            for (int i = 1; i <= n; i++) {
                if (graph[v][i] == 1 && ch[i] != 1) {
                    ch[i] = 1;
                    DFS(i);
                    // DFS 빠져나오면 그 정점 check배열 0으로 해주기
                    ch[i] = 0;
                }
            }
        }
    }


    public static void main(String args[]) {

        path_finding_adjacency_matrix T = new path_finding_adjacency_matrix();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int m = sc.nextInt();

        graph = new int[n+1][n+1];

        for (int i = 0; i < m; i++) {
            graph[sc.nextInt()][sc.nextInt()] = 1;
        }

        ch = new int[n+1];

        // 1에서 시작
        ch[1] = 1; 
        T.DFS(1);
        System.out.println(answer);


       sc.close();
    }
    
}
