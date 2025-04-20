// 최단거리 -> BFS -> Queue -> Node로 Level 탐색
import java.util.*;

class Node {
    int data;
    Node lt,rt;
    public Node(int data) {
        this.data = data;
        lt = rt = null;
    }
}

public class graph_shortest_path {

    Node root;

    public void BFS(Node root) {
        
        if (root == null) return;
        else {
            int L = 0;
            Queue<Node> Q = new LinkedList<>();
            Q.offer(root);

            while (!Q.isEmpty()) {
                int size = Q.size();
                for (int i = 0; i < size; i++) {
                    Node cur = Q.poll();
                    if (cur.data != 1) {
                        System.out.println(cur.data + " : " + L);
                    }
                    if (cur.lt != null) Q.offer(cur.lt);
                    if (cur.rt != null) Q.offer(cur.rt);
                }
                L++;
            }
        }
    }

    public static void main(String args[]) {

        graph_shortest_path T = new graph_shortest_path();
        T.root = new Node(1);
        T.root.lt = new Node(3);
        T.root.rt = new Node(4);
        T.root.rt.lt = new Node(5);
        T.root.rt.rt = new Node(6);
        T.root.rt.rt.lt = new Node(2);

        T.BFS(T.root);
    }
}
