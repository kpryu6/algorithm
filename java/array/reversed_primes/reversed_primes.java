package array.reversed_primes;

import java.util.Scanner;

public class reversed_primes {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // StringBuilder로 입력받자마자 reverse
        StringBuilder[] arrReverse = new StringBuilder[n];
        for (int i = 0 ; i < n; i++) {
            arrReverse[i] = new StringBuilder(sc.next()).reverse();
        }

        // 23 55 26 02 052 073 002 03 001

        // primes에 arrReverse 넣기
        int[] primes = new int[n];
        for (int i = 0 ; i < n; i++) {
            // Integer.parseInt(String) 이기 때문에 toString 해줌
            primes[i] = Integer.parseInt(arrReverse[i].toString());
        }
        
        // 23 55 26 2 52 73 2 3 1

        // 효율 쓰레긴데? ㅠㅠ
        
        for (int i = 0; i < n; i++) {
            // 나머지 0으로 초기화
            int rest = 0;

            // 약수가 1과 자기자신밖에 없으면 소수
            // But 반대로 2부터 자기자신 전까지로 해서 나눠지는게 없으면 소수 라고 해도됨. -> reversed_primes_easy.java 참고
            for (int j = 1 ; j <= primes[i]; j++) {
                if (primes[i] % j == 0) rest++;
            }
            if (rest == 2) System.out.print(primes[i] + " ");

        }
        
        sc.close();

    }
    
}
