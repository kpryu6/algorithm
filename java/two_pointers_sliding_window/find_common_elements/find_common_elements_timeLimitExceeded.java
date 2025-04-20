
// Time Limit Exceeded

package two_pointers_sliding_window.find_common_elements;

import java.util.Scanner;
import java.util.ArrayList;

public class find_common_elements_timeLimitExceeded {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr1 = new int[n];
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        int m = sc.nextInt();
        int[] arr2 = new int[m];
        for (int i = 0; i < n; i++) {
            arr2[i] = sc.nextInt();
        }

        ArrayList<Integer> common = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr1[i] == arr2[j]) common.add(arr1[i]);
            }
        }

        // ArrayList 오름차순으로 정렬
        for (int i = 0; i < common.size(); i++) {
            for (int j = i + 1; j < common.size(); j++) {
                if (common.get(i) > common.get(j)) {
                    int temp = common.get(j);
                    common.set(j, common.get(i));
                    common.set(i, temp);
                }
            }
        }

        for (int x : common) System.out.print(x + " ");


        sc.close();

    }
    
}
