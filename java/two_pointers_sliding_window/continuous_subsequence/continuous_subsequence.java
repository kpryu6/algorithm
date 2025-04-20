package two_pointers_sliding_window.continuous_subsequence;

import java.util.Scanner;

public class continuous_subsequence {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int lt = 0, rt = 0;
        int sum = arr[0];
        int answer = 0;

        while (rt < N) {
            if (sum < M) {
                // indexOutofRange 방지
                if (rt < N-1) sum += arr[++rt];
                else break;
            }
            else if (sum > M) {
                // lt가 rt를 추월하는 것을 방지
                if (lt < rt) sum -= arr[lt++];
                else break;
            }
            else if (sum == M) {
                answer++;
                // lt가 rt를 추월하는 것을 방지
                if (lt < rt) sum -= arr[lt++];
                else break;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}
