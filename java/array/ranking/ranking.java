package array.ranking;

// 정렬 문제인가? ㄴㄴ 
// 중복을 어떻게 해결할 것인가?
import java.util.Scanner;

public class ranking {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // ** arr를 돌면서 바로바로 등수를 구하자. **

        // 등수를 저장하는 배열
        int[] ranking = new int[n];

        for (int i = 0; i < n; i++) {
            // 등수
            int rank = 1;

            for (int j = 0; j < n; j++) {
                if (arr[i] < arr[j]) rank++;
            }
            ranking[i] = rank;
        }

        for (int x : ranking) System.out.print(x + " ");

        sc.close();
    }
    
}
