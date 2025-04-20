package dfs_bfs_hard.badook;

import java.util.*;

public class badook {

    static int C,n,answer = 0;
    static int[] arr;

    public void DFS(int L, int sum) {

        if (sum > C) return;
        if (L == n) {
            answer = Math.max(answer, sum);
        }
        else {
            DFS(L+1, sum + arr[L]);
            DFS(L+1, sum);
        }
    }

    public static void main(String args[]) {

        badook T = new badook();
        Scanner sc = new Scanner(System.in);

        C = sc.nextInt();
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        T.DFS(0,0);
        System.out.println(answer);
        sc.close();
    }
    
}
