    import java.util.*;

    class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public class point_sorting {

        public Point[] solution (int n, Point[] points) {

            for (int i = 0; i < n-1; i++) {
                for (int j = i+1; j < n; j++) {
                    if (points[i].x > points[j].x || 
                        points[i].x == points[j].x && points[i].y > points[j].y) {

                            // Point 자체 교환
                            // Point 안에 있는 x, y를 교환 하면 n이 큰 수 일때 오류..
                            Point tmp = points[i];
                            points[i] = points[j];
                            points[j] = tmp;
                        
                    }
                    
                }
            }
            return points;

        }

        public static void main(String args[]) {
            
            point_sorting T = new point_sorting();
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();

            Point[] points = new Point[n];

            for (int i = 0; i < n; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                points[i] = new Point(x, y);
            }

            Point[] answer = T.solution(n,points);
            for (int i = 0; i < n; i++) {
                System.out.print(answer[i].x + " " + answer[i].y);
                System.out.println();
            }
            sc.close();

        }
        
    }
