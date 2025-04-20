import java.util.*;

// Comparable Interface
class Point implements Comparable<Point> {
    public int x,y;
    public Point (int x, int y) {
        this.x = x;
        this.y = y;
    }
    // 음수면 오름차순, 양수면 내림차순
    @Override
    public int compareTo (Point o) {
        if (this.x == o.x) return this.y - o.y;
        else return this.x - o.x;
    }
}

public class point_sorting_comparable {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        ArrayList<Point> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            list.add(new Point(x,y));
        }
        // 이걸로 정렬
        Collections.sort(list);

        for (Point x : list) {
            System.out.println(x.x + " " + x.y);
        }
        sc.close();
    }
    
}
