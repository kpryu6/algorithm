package array.fibonacci;

import java.util.Scanner;

public class fibonacci {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] fibonacci = new int[n];
        fibonacci[0] = 1;
        fibonacci[1] = 1;

        for (int i = 2; i < n; i++) {
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
        }

        for (int x : fibonacci) {
            System.out.print(x + " ");
        }
        
        sc.close();

    }
    
}
