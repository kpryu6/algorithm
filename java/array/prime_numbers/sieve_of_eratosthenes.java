
// 에라토스테네스의 체
package array.prime_numbers;

import java.util.Scanner;
// import java.util.Arrays;


public class sieve_of_eratosthenes {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] numbers = new int[n+1];
        // 배열 0으로 다 채우기 but 바로 위 코드는 모두 0으로 초기화 자동으로 시켜줌
        // Arrays.fill(numbers,0);
        int answer = 0;
        
        for (int i = 2; i <= n; i++) {
            // 소수 찾기 (0이면 소수)
            if (numbers[i] == 0) {
                answer++;
                // i가 소수면 i의 배수 모두 소수가 아니므로 제외 (1로 만들기)
                for (int j = i; j <= n; j = j + i){
                    numbers[j] = 1;
                }
            }
        }

        System.out.println(answer);
        sc.close();
    }
    
}
