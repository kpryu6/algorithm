package two_pointers_sliding_window.sum_of_consecutive_numbers;

import java.util.Scanner;

public class sum_of_consecutive_numbers{

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;

        for (int i = 1; i <= n/2; i++) {
            int sum = 0;
            for (int j = i; j<= n/2 + 1; j++) {
                sum += j;
                if (sum == n) {
                    answer++;
                    break;
                }
            }
        }
        System.out.println(answer);
        sc.close();

    }
}