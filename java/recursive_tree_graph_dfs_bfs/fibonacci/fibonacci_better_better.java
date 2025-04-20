
import java.util.*;

public class fibonacci_better_better {

    // 재귀는 스택프레임을 쓰기 때문에 for문보다 성능이 안좋다.
    // 메모이제이션
    static int[] fibo;
    public int DFS(int n) {

        if (fibo[n] > 0) return fibo[n];    // 요거 하나 차이
        // 트리의 오른쪽이 뻗어나갈때 다시 재귀안하고 왼쪽에서 구한것을 쓰면됨.
        if (n == 1) return fibo[n] = 1;
        else if (n == 2) return fibo[n] = 1;
        else return fibo[n] = DFS(n-2) + DFS(n-1);
    }

    public static void main(String args[]) {

        fibonacci_better_better T = new fibonacci_better_better();
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
