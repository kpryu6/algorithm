
//time limit Exceeded
// ¿Ã¡ﬂ forπÆ
package two_pointers_sliding_window.continuous_subsequence;

import java.util.Scanner;

public class continuous_subsequence_time_limit_Exceeded {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int answer = 0;
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            cnt = 0;
            for (int j = i; j < N; j++) {
                cnt += arr[j];
                if (cnt == M) {
                    answer++;
                    break;
                }

            }
        }

        System.out.println(answer);

        sc.close();
    }

    
}
