import java.util.Scanner;

    // 삽입 정렬 (Insertion Sort)은 각 원소를 이미 정렬된 부분과 비교하여 적절한 위치에 삽입하는 방법
    public class insertion_sort {

        public static void main(String args[]) {

            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            for (int i = 1; i < n; i++) {
                for (int j = i; j > 0; j--) {
                    if (arr[j] < arr[j-1]) {
                        int tmp = arr[j];
                        arr[j] = arr[j-1];
                        arr[j-1] = tmp;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                System.out.print(arr[i] + " ");
            }
            sc.close();
        }
        
    }
