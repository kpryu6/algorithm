import java.util.*;

class Node {
    int data;
    Node lt,rt;
    public Node (int data) {
        this.data = data;
        lt = rt = null;
    }
}

public class shortest_path{

    public int BFS(Node root) {

        int L = 0;
        if (root == null) return 0;
        else {
            Queue<Node> Q = new LinkedList<>();
    
            Q.offer(root);
            while(!Q.isEmpty()) {
                int size = Q.size();
                for (int i = 0; i < size; i++) {
                    Node cur = Q.poll();
                    if(cur.lt== null && cur.rt== null) return L;
                    else if (cur.lt != null) Q.offer(root.lt);
                    else if (cur.rt != null) Q.offer(root.rt);
                }
                L++;
            }
            
        }
        return 0;
    } 

    

    public static void main(String args[]) {

        shortest_path T = new shortest_path();
        Node root = new Node(1);
        root.lt = new Node(2);
        root.rt = new Node(3);
        root.lt.lt = new Node(4);
        root.lt.rt = new Node(5);
        System.out.println(T.BFS(root));
    }
    
}
