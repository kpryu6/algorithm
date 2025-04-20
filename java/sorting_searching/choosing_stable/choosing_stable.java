package sorting_searching.choosing_stable;

import java.util.*;

public class choosing_stable {

    // 말 놓기 
    public int count (int[] arr, int distance) {

        int cnt = 1;
        int ep = arr[0];

        for (int x : arr) {
            // 거리가 되면 말 놓기
            if (x - ep >= distance) {
                ep = x;
                cnt++;
            }
        }

        return cnt;
    }

    public int solution (int n, int m, int[] arr) {

        int answer = 0;
        // 거리의 최소값 lt
        int lt = 1;
        // 거리의 최대값 rt
        int rt = Arrays.stream(arr).max().getAsInt();

        // 정렬
        Arrays.sort(arr);

        while (lt <= rt) {

            int mid = (lt + rt) / 2;

            if (count(arr,mid) >= m) {
                answer = mid;
                lt = mid + 1;
            }
            else rt = mid - 1;

        }
        return answer;

    }

    public static void main(String args[]) {

        choosing_stable T = new choosing_stable();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(n,m,arr));
        sc.close();
    }
    
}
