package array.temporary_leader;

import java.util.Scanner;

public class temporary_leader {

    public static void main (String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][5];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        
        // 각 학생의 같은 반 존재 count
        int[] cnt = new int[n];

        // *************** 이 부분만 다름 *********************

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                for (int k = 0; k < 5; k++) {
                    // i번 학생의 k학년과 j번 학생의 k학년이 같을 때
                    if (arr[i][k] == arr[j][k]) {
                        cnt[i]++;
                        break;
                    }
                }
            }
        }
      
        // *************** 이 부분만 다름 *********************


        int max = Integer.MIN_VALUE;

        // cnt가 제일 큰 경우 출력
        for (int i = 0; i < n; i++) {
            max = Math.max(max,cnt[i]);
        }

        // 같을 경우 제일 작은 번호를 뽑아야 함
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            if (cnt[i] == max) {
                // index니까 +1
                min = Math.min(min,i+1);
            }
        }
        System.out.println(min);

        sc.close();
    }
    
}
