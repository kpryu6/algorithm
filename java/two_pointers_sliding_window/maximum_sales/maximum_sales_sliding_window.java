
// O(n)
package two_pointers_sliding_window.maximum_sales;

import java.util.Scanner;

public class maximum_sales_sliding_window {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        // n일 간의 매출기록
        int n = sc.nextInt();
        // 연속된 m일
        int m = sc.nextInt();

        int[] history = new int[n];
        for (int i = 0; i < n; i++) {
            history[i] = sc.nextInt();
        }
        
        // Sliding Window 기법 사용 : 한 번에 하나의 요소만 추가하고 제거하여 이전 합을 재사용
        // 처음 m일 합을 구하고 그다음부터는 m+1번째 더하고 첫번째꺼 빼고 이런 방식
        // sum에 1 2 3 있었으면 그다음은 2 3 4 그다음은 3 4 5

        int sum = 0;
        // history[0] + history[1] + history[2]
        for (int i = 0; i < m; i ++) {
            sum += history[i];
        }

        // max를 처음 3개 합으로
        int max = sum;

        for (int i = m; i < n; i ++) {
            sum += history[i] - history[i-m];
            max = Math.max(max,sum);
        }
        
        System.out.println(max);
        sc.close();
    }
    
}
