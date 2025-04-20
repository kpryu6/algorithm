package array.peak;

import java.util.Scanner;

public class peak {

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
        
        // 봉우리 확인
         for (int i = 1; i < n+1; i++) {
            int max = 0;
            for (int j = 1; j < n+1; j++) {
                // 같은 것이 있으면 봉우리가 아니기때문에 break
                max = Math.max(arr[i][j],arr[i-1][j]); // 상
                if (arr[i][j] == arr[i-1][j]) continue;
                max = Math.max(max,arr[i+1][j]); // 하
                if (arr[i][j] == arr[i+1][j]) continue;
                max = Math.max(max,arr[i][j-1]); // 좌
                if (arr[i][j] == arr[i][j-1]) continue;
                max = Math.max(max,arr[i][j+1]); // 우
                if (arr[i][j] == arr[i][j+1]) continue;

                if (max == arr[i][j]) answer++;
            }
        }

        System.out.println(answer);
        


        sc.close();
    }
    
}
