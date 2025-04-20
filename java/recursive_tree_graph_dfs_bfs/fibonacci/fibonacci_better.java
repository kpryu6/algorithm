
import java.util.*;

public class fibonacci_better {

    // static 배열에 저장 (DFS(n) 한번 실행)
    static int[] fibo;
    public int DFS(int n) {

        if (n == 1) return fibo[n] = 1;
        else if (n == 2) return fibo[n] = 1;
        else return fibo[n] = DFS(n-2) + DFS(n-1);
    }

    public static void main(String args[]) {

        fibonacci_better T = new fibonacci_better();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        fibo = new int[n+1];
        T.DFS(n);
        for (int i = 1; i <= n; i++) {
            System.out.print(fibo[i] + " ");
        }
        sc.close();
    }
    
}
