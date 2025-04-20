package array.temporary_leader;

/* 
즉 1번 학생과 같은 반을 한 학생을 카운팅 할 때 3번 학생이 1번 학생과 1학년때와 2학년때 같은 반을 
   두 번 했더라도 3번 학생을 한 번만 카운팅해야 합니다.
   => 다른 학생과 한번이라도 같은 반 했으면 그 이후로 같은 반 했어도 카운트 X
*/
import java.util.Scanner;

public class temporary_leader_easy {

    public int solution(int n, int[][] arr) {

        int answer = 0;
        int max = Integer.MIN_VALUE;
        // i = 1 -> 1학년 때 같은 반 한 학생들
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                if (i == j) continue;
                for (int k = 1; k <= 5; k++) {
                    // i번 학생의 k학년과 j번 학생의 k학년이 같을 때
                    if (arr[i][k] == arr[j][k]) {
                        // cnt는 최대 4겠네 그럼
                        cnt++;
                        break;
                }
                }
            }
            if (cnt > max) {
                max = cnt;
                answer = i;
            }
        }

        return answer;
    }

    public static void main(String args[]) {

        temporary_leader_easy T = new temporary_leader_easy();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n+1][6];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= 5; j++) {
                arr[i][j] = sc.nextInt();
            }
        }


        System.out.println(T.solution(n,arr));
        sc.close();
    }
    
}
