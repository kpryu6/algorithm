// 3 입력시 1 2 3 출력
import java.util.*;

public class recursive_function {

    // stack frame
    // back tracking
    public void DFS(int n) {

        if (n == 0) return;
        else {
            DFS(n-1);
            System.out.print(n + " ");
        }
        
        

    }

    public static void main(String args[]) {

        recursive_function T = new recursive_function();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        T.DFS(n);
        sc.close();

    }
    
}
