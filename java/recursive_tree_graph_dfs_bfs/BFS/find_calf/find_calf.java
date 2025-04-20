// time limit exceeded
import java.util.*;

class Node {
    int data;
    Node rt, lt, mid;
    public Node(int data) {
        this.data = data;
        lt = rt = mid = null;
    }
}
public class find_calf {

    public int BFS(Node root, Node destination) {

        int L = 0;
        if (root == null) return 0;
        else {
            Queue<Node> Q = new LinkedList<>();
            
            Q.offer(root);

            while (!Q.isEmpty()) {

                // System.out.print("Level " + L + " : ");
                int size = Q.size();

                for (int i = 0; i < size; i++) {
                    Node cur = Q.poll();
                    // System.out.print(cur.data + " ");
                    if (cur.data != destination.data) {
                        Q.offer(new Node(cur.data-1));
                        Q.offer(new Node(cur.data+1));
                        Q.offer(new Node(cur.data+5));
                    }
                    else {
                        Q.clear();
                        return L;
                    }
                }

                L++;
                // System.out.println();
            }
        }
        return 0;


    }

    public static void main(String args[]) {
        
        find_calf T = new find_calf();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int calf = sc.nextInt();

        Node root = new Node(n);
        Node destination = new Node(calf);

        System.out.println(T.BFS(root,destination));
        sc.close();
    }
    
}
