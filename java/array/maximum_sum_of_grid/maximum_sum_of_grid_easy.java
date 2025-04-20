package array.maximum_sum_of_grid;

import java.util.Scanner;

public class maximum_sum_of_grid_easy {

    public int solution(int n, int arr[][]) {

        int answer = Integer.MIN_VALUE;
        int sum1, sum2;

        // 행 합의 최대값과 열 합의 최대값을 한번에 비교
        for (int i = 0; i < n; i++) {
            sum1 = sum2 = 0;
            for (int j = 0; j < n; j++) {
                sum1 += arr[i][j];
                sum2 += arr[j][i];
            }
            answer = Math.max(answer, sum1);
            answer = Math.max(answer, sum2);
        }

        sum1 = sum2 = 0;
        // 대각선 비교
        for (int i = 0; i < n; i++) {
            // X의 \
            sum1 += arr[i][i];
            // X의 /
            sum2 += arr[i][n-i-1];
        }

        answer = Math.max(answer, sum1);
        answer = Math.max(answer, sum2);
        return answer;
    }

    public static void main(String args[]) {

        maximum_sum_of_grid_easy T = new maximum_sum_of_grid_easy();        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j]= sc.nextInt();
            }
        }
        System.out.println(T.solution(n,arr));
        sc.close();
    }
    
}
