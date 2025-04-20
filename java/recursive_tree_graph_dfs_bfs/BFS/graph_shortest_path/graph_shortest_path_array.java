import java.util.*;

public class graph_shortest_path_array {

    static int n,m;
    static ArrayList<ArrayList<Integer>> graph; 
    static int[] ch, dis;

    public void BFS(int v) {
        Queue<Integer> Q = new LinkedList<>();
        ch[v] = 1;
        dis[v] = 0;
        Q.offer(v);
        while(!Q.isEmpty()) {
            int cv = Q.poll();
            for (int nv : graph.get(cv)) {
                if (ch[nv] == 0) {
                    ch[nv] = 1;
                    Q.offer(nv);
                    // + Level
                    dis[nv] = dis[cv] + 1;
                }
            }
        }
    }


    public static void main(String args[]) {

        graph_shortest_path_array T = new graph_shortest_path_array();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // ArrayList ¸¸µé±â
        graph = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            graph.get(sc.nextInt()).add(sc.nextInt());
        }
        ch = new int[n+1];
        dis = new int[n+1];

        T.BFS(1);

        for (int i = 2; i <= n; i++) {
            System.out.println(i + " : " + dis[i]);
        }

        sc.close();
    }
    
}
