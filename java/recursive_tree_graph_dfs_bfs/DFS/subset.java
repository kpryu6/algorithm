import java.util.*;

public class subset {

    static int n;
    static int[] ch;

    public void DFS(int L) {

        if (L == n+1) {
            // ch에 1로 체크된 인덱스 출력
            for (int i = 1; i <= n; i++) { 
                if (ch[i] == 1) System.out.print(i + " ");
            }
            System.out.println();

        }
        else {
            // 사용
            ch[L] = 1;
            // 왼쪽
            DFS(L+1);
            // 사용 X
            ch[L] = 0;
            // 오른쪽
            DFS(L+1);
        }

    }

    public static void main(String args[]) {

        subset T = new subset();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        // ch배열의 인덱스 번호가 원소
        ch = new int[n+1];
        T.DFS(1);
        sc.close();
    }
    
}
