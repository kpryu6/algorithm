import java.util.*;
public class practice {

    static String answer = "NO";
    static int n,total = 0;
    static int arr[];
    boolean flag = false;

    public void DFS(int L, int sum) {
        
        if (sum > (total/2)) return;
        if (flag) return;
        if (L == n){
            if (sum == (total/2)) {
                answer = "YES";
                flag = true;
            }
        }
        else {
            DFS(L+1,sum+arr[L]);
            DFS(L+1,sum);
        }

    }

    public static void main(String args[]) {

        practice T = new practice();
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        arr = new int[n+1];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        T.DFS(0,0);
        System.out.println(answer);
        sc.close();
    }
    
}
