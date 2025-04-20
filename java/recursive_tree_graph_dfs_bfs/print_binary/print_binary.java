// 재귀함수를 이용한 이진수 출력
// 11 입력
// 1011 출력
import java.util.*;

public class print_binary {

    public void DFS (int n) {

        if (n == 0) return;
        else {
            DFS(n/2);
            System.out.print(n%2);
        }

    }

    public static void main(String args[]) {

        print_binary T = new print_binary();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        T.DFS(n);
        sc.close();
    }
    
}
