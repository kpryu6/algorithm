package array.peak;

import java.util.Scanner;

public class peak_easy {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n+2][n+2];

        for (int i = 0; i < n+2; i++) {
            for (int j = 0; j < n+2; j++) {
                // 전체 0만들기
                arr[i][j] = 0;
            }
        }

        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                // 입력받기
                arr[i][j] = sc.nextInt();
            }
        }

        // -----가장자리 0으로 채우기 완성-------

        // 봉우리 수
        int answer = 0;
        
        // 상하좌우 보기 위해 만듦
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        // 봉우리 확인
         for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                // 봉우리면 true
                boolean flag = true;

                for (int k = 0; k < 4; k++) {
                    // 상하좌우 한번에 보고 자신보다 크거나 같으면 봉우리 아님
                    if (arr[i + dx[k]][j + dy[k]] >= arr[i][j] ){
                        flag = false;
                        break;
                    }
                }
                if (flag) answer++;
            }
        }

        System.out.println(answer);
        


        sc.close();
    }
    
}
