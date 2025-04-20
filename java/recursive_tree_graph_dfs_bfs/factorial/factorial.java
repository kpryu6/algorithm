import java.util.Scanner;

public class factorial {

    public int fact (int n) {

        if (n == 1) return 1;
        else  return n * fact(n-1);
        

    }

    public static void main(String args[]) {

        factorial T = new factorial();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(T.fact(n));
        sc.close();
    }
    
}
