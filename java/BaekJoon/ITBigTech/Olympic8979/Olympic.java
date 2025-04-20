import java.util.*;
import java.io.*;

public class Olympic {
    public static void main(String args[]) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken()); // 국가 수
        int K = Integer.parseInt(st.nextToken()); // 순위를 알고싶은 국가
        int endPoint = 0;

        ArrayList<Node> list = new ArrayList<>();

        while(N --> 0) {
            st = new StringTokenizer(br.readLine(), " ");
            int num = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());

            list.add(new Node(num, gold, silver, bronze, 0));
        }

        Collections.sort(list);
        list.get(0).rank = 1; // 정렬 후 리스트 첫번째 국가가 1등

        // 등수 매겨주기
        for (int i = 1; i < list.size(); i++) {
            Node current = list.get(i);

            int prevG = list.get(i-1).g;
            int prevS = list.get(i-1).s;
            int prevB = list.get(i-1).b;

            // 국가 번호가 K면 endPoint
            if (list.get(i).num == K) {
                endPoint = i;
            }

            // 공동 순위
            if (current.g == prevG && current.s == prevS && current.b == prevB) {
                list.get(i).rank = list.get(i-1).rank;
            } // 아니면
            else {
                list.get(i).rank = i + 1;
            }
        }
        System.out.println(list.get(endPoint).rank);
    }
}

class Node implements Comparable<Node> {
    int num, g, s, b, rank;

    Node(int num, int g, int s, int b, int rank) {
        this.num = num;
        this.g = g;
        this.s = s;
        this.b = b;
        this.rank = rank;
    }

    // 메달, 내림차순 정렬
    @Override
    public int compareTo(Node n) {
        if (this.g == n.g) {
            if (this.s == n.s) {
                return n.b - this.b;
            } else {
                return n.s - this.s;
            }
        } else {
            return n.g - this.g;
        }
    }
}