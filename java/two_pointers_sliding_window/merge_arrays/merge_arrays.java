package two_pointers_sliding_window.merge_arrays;

import java.util.Scanner;

public class merge_arrays {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        
        // 입력받기
        int n1 = sc.nextInt();
        int[] arr1 = new int[n1];
        for (int i = 0; i < n1; i++) {
            arr1[i] = sc.nextInt();
        }

        int n2 = sc.nextInt();
        int[] arr2 = new int[n2];
        for (int i = 0; i < n2; i++) {
            arr2[i] = sc.nextInt();
        }

        // 일단 합치기
        int[] arrAdd = new int[n1+n2];
        for (int i = 0; i < n1; i++) {
            arrAdd[i] = arr1[i];
        }
        for (int i = 0; i < n2; i++) {
            arrAdd[i+n1] = arr2[i];
        }

        // 순서대로 정렬하기
        // Arrays.sort(arrAdd);
        // 다시 풀어보기
        for (int i = 0; i < n1 + n2 - 1; i++) {
            for (int j = i + 1; j < n1 + n2; j++) {
                if (arrAdd[i] > arrAdd[j]) {
                    int temp = arrAdd[j];
                    arrAdd[j] = arrAdd[i];
                    arrAdd[i] = temp;
                }
            }
        }
   
        for (int x : arrAdd) System.out.print(x + " ");
        sc.close();
    }
    
}
