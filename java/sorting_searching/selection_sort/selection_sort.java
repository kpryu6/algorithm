import java.util.*;

// 선택 정렬(Selection Sort)은 주어진 리스트에서 최솟값을 찾아 맨 앞에 위치한 값과 교체하고, 
// 그 다음으로 작은 값을 찾아 두 번째 위치한 값과 교체하는 과정을 반복하여 정렬하는 알고리즘
public class selection_sort {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        sc.close();
    }
    
}
