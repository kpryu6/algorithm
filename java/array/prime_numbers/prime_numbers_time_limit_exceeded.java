
// Time Limit Exceeded
package array.prime_numbers;

import java.util.Scanner;

public class prime_numbers_time_limit_exceeded {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;

        // 소수란 1과 자신 말고는 나머지가 0이 아님

        for (int i = 2; i <= n; i++) {

            // 나머지가 0일때 증가
            int rest = 0;

            for (int j = 1; j <= i; j++) {
                
                if (i%j == 0) rest++;
            }

            // 소수는 나머지가 0일때가 2번
            if (rest == 2) answer++;
        }

        System.out.println(answer);
        sc.close();

    }
    
}
