package array.maximum_sum_of_grid;

import java.util.Scanner;

public class maximum_sum_of_grid {

    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int [][] arr = new int [n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        // 행 초기화
        int[] rowSum = new int[n];

        // 행 최대값
        int rowMax = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rowSum[i] += arr[i][j];
            }
            if (rowMax < rowSum[i]) rowMax = rowSum[i];
        }


        // 열 초기화
        int[] columnSum = new int[n];

        // 열 최대값
        int columnMax = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                columnSum[i] += arr[j][i];
            }
            if (columnMax < columnSum[i]) columnMax = columnSum[i];
        }


        // 두 대각선 초기화
        int[] crossSum = new int[2];
        // X 부분의 \
        for (int i = 0; i < n; i++) {
            crossSum[0] += arr[i][i];
        }
        // X 부분의 /
        for (int i = 0; i < n; i++) {
            int j = n - 1;
            crossSum[1] += arr[i][j];
            j--;
        }
        // 두 대각선 중에 큰 거
        int crossMax = crossSum[0] < crossSum[1] ? crossSum[1] : crossSum[0];

        // 각각의 Max 끼리 비교해서 큰거
        int finalMax = (rowMax > columnMax) ? (rowMax > crossMax ? rowMax : crossMax) : (columnMax > crossMax ? columnMax : crossMax);


        System.out.println(finalMax);

        sc.close();
    
    }

    
}
