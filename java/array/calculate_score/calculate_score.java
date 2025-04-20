package array.calculate_score;

import java.util.Scanner;

public class calculate_score {

    public int solution(int n, int[] arr) {

        // 총 점수
        int answer = 0;
       
        for (int i = 0; i < n; i ++) {
            // 점수
            int plus = 0;

            // arr[i]가 1이면 다음 인덱스 보면서 계속 1이면 plus++
            if (arr[i] == 1) {
                while (arr[i] == 1) {
                    i++; // 인덱스 증가
                    plus++; // 가산점
                    // answer에 plus 누적하기 
                    answer += plus;
                    // i가 마지막 인덱스보다 커지면 나오기
                    if (i == n) break;
                }
            }
            else {
                // arr[i]가 0이면 다음 인덱스로 넘어가기
                continue;
            }
        }

        return answer;
    }

    public static void main(String args[]) {

        calculate_score T = new calculate_score();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println(T.solution(n,arr));

        sc.close();

    }
    
}
