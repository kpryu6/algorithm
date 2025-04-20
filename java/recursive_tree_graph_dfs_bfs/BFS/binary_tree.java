import java.util.*;

// 레벨 탐색 (Queue 사용)
// 1 / 2 3 / 4 5 6 7

class Node {
    int data;
    Node rt, lt;
    public Node (int data) {
        this.data = data;
        lt = rt = null;
    }
}
public class binary_tree {

    Node root;
    public void BFS(Node root) {

        if (root == null) return;
        else {
            Queue<Node> Q = new LinkedList<>();
            Q.offer(root);
            // Level
            int L = 0;

            while (!Q.isEmpty()) {
                // size 선언안하고 for문에 그대로 Q.size() 했더니 오류났음
                /*
                 * 예를 들어, 큐에 노드 2개가 들어있을 때, 큐의 사이즈는 2입니다. 
                 * 하지만 첫 번째 노드를 꺼내면서 그 자식 노드들을 큐에 넣으면, 큐의 사이즈는 3이 됩니다. 
                 * 이 상태에서 반복문이 다시 실행되면, 큐의 사이즈가 3이 되어버리기 때문에 예상치 못한 결과가 나오게 됩니다.
                 */
                int size = Q.size();

                System.out.print("Level " + L + " : ");

                for (int i = 0; i < size; i++) {
                    Node cur = Q.poll();
                    System.out.print(cur.data + " ");
                    if (cur.lt != null) Q.offer(cur.lt);
                    if (cur.rt != null) Q.offer(cur.rt);
                }

                L++;
                System.out.println();
            }

        }

    }

    public static void main(String args[]) {

        binary_tree T = new binary_tree();
        T.root = new Node(1);
        T.root.lt = new Node(2);
        T.root.rt = new Node(3);
        T.root.lt.lt = new Node(4);
        T.root.lt.rt = new Node(5);
        T.root.rt.lt = new Node(6);
        T.root.rt.rt = new Node(7);
        T.BFS(T.root);
    }
    
}
