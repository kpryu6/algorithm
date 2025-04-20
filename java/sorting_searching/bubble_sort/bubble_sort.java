import java.util.Scanner;

    // 버블 정렬(Bubble Sort)은 인접한 두 개의 원소를 비교하여 정렬하는 알고리즘
    public class bubble_sort {

        public static void main(String args[]) {

            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            for (int i = 0; i < n-1; i++) {
                for (int j = 0; j < n-1-i; j++) {
                    if (arr[j] > arr[j+1]) {
                        int tmp = arr[j+1];
                        arr[j+1] = arr[j];
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
