package string.char_distance;

import java.util.Scanner;

public class char_distance_easy {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] inputs = input.split(" ");
        String str = inputs[0];
        char ch = inputs[1].charAt(0);

        // 왼쪽의 ch로 부터 떨어진 거리와 오른쪽의 e로 부터 떨어진 거리를 비교해서 구하기
        char[] strArray = str.toCharArray();
        int n = str.length();
        int p = 1000;

        // 떨어진 거리를 저장하는 int 배열
        int[] intArr = new int[n];

        // 왼쪽의 ch로부터 떨어진 거리
        for (int i = 0; i < n; i++) {
            
            if (strArray[i] == ch) {

                p = 0;
            }
            intArr[i] = p;
            p++;
        }

        /*  for (int x : intArr) {
            System.out.print(x + " ");
        }
        System.out.println(); */


        // 왼쪽의 ch로부터 떨어진 거리
        for (int i = n-1; i >= 0; i--) {
            
            if (strArray[i] == ch) p = 0;
            
            intArr[i] = Math.min(intArr[i],p);
            
            p++;
        }

         for (int x : intArr) {
            System.out.print(x + " ");
        }
        sc.close();

    }
    
}
