package array.calculate_score;

import java.util.Scanner;

public class calculate_score_easy {

    public int solution(int n, int[] arr) {

       int answer = 0, cnt = 0;

       for (int i = 0; i < n; i++) {

        if (arr[i] == 1) {
            // 뭐 인덱스 증가 이런거 필요 없음
            cnt++;
            answer += cnt;
        }
        else {
            cnt = 0;
        }
       }
       return answer;
    }

    public static void main(String args[]) {

        calculate_score_easy T = new calculate_score_easy();
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
