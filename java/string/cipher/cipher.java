package string.cipher;

import java.util.Scanner;

public class cipher {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String input = sc.next();
        char[] inputArray = input.toCharArray();
        char[] answer = new char[n];

        // input을 이진수로 바꾸기
        for (int i = 0; i < input.length(); i++) {

            if (input.charAt(i) == '#') inputArray[i] = '1';
            else inputArray[i] = '0';

        }

        // 2진수로 바꾼 Input 다시 String
        String inputTwoDecimal = String.valueOf(inputArray);

        int[] codes = new int[n];

        for (int i = 0; i < n; i++) {
            // 7개씩 나눠서 2진수의 값을 10진수로 변경
            codes[i] = Integer.parseInt(inputTwoDecimal.substring(7*i, 7*(i+1)),2);
            // 10진수의 값들을 char로 변경
            answer[i] = (char) codes[i];
            System.out.print(answer[i]);
            
        }
        sc.close();

    }
    
}
