package array.peak;

import java.util.Scanner;

public class peak_not_extended_table {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 입력받기
                arr[i][j] = sc.nextInt();
            }
        }

        // 봉우리 수
        int answer = 0;
        
        // 상하좌우 보기 위해 만듦
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        // 봉우리 확인
         for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 봉우리면 true
                boolean flag = true;

                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    
                    // 상하좌우 한번에 보고 자신보다 크거나 같으면 봉우리 아님
                    if (nx>=0 && ny>=0 && nx<n && ny<n && arr[nx][ny] >= arr[i][j]){
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
