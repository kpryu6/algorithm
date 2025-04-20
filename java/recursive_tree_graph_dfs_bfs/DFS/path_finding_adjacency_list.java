// 정점이 많아지면 비효율적인 인접행렬을 대신하여 인접리스트로
import java.util.*;
public class path_finding_adjacency_list {

    static int n,m,answer=0;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] ch;
    public void DFS(int v) {

        if (v == n) answer++;
        else {
            for (int nv : graph.get(v)) {
                if (ch[nv] == 0) {
                    ch[nv] = 1;
                    DFS(nv);
                    ch[nv] = 0;
                }
            }
        }

    }


    public void DFS()

    public static void main(String args[]) {
        
        path_finding_adjacency_list T = new path_finding_adjacency_list();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        
        graph = new ArrayList<ArrayList<Integer>>();
        // n까지 참조해야하니까 n까지
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }
        ch = new int[n+1];
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            // 알고리즘 깜지 12페이지
            graph.get(a).add(b);
        }
        ch[1]=1;
        T.DFS(1);
        System.out.println(answer);

        


    }
    
}
