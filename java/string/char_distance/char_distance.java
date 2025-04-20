package string.char_distance;

import java.util.Scanner;

public class char_distance {

    public static void main (String arg[]) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] inputs = input.split(" ");

        // input 분리
        String str = inputs[0];
        char ch = inputs[1].charAt(0);

        

        // index를 표현해주기 위한 intArray
        int [] intArr = new int[str.length()];
        
        // str 안에 있는 ch의 수
        int n = 0;
        
        for (int i = 0; i < str.length(); i++) {

            // ch와 같은 문자를 가진 값은 0으로 초기화
            if (str.charAt(i) == ch) {
                intArr[i] = 0; n++;
            }
            else {
                intArr[i] = 1;
            }
            // 나머지에 대한 index 저장
            // 0이 들어있는 배열의 인덱스를 어떻게 추출할까?
        }
        // n = 3
        // intArr -> ex) 0 1 1 1 0 1 0 1 

        // intArr에서 0을 가진 index를 targetIndex에 저장
        int[] targetIndex = new int[n];
        int index = 0;

        for (int i = 0; i < str.length(); i++) {

            if (intArr[i] == 0) {
                targetIndex[index] = i; index++;
            }
            
        }

      
        int[] subtractIndex = new int[n];

        for (int i = 0; i < str.length(); i++) {

            int tmp = Integer.MAX_VALUE;

            // index 차이를 배열로 만들기
            for (int j = 0; j < n; j++){

               subtractIndex[j] = Math.abs(i-targetIndex[j]);
            
            }

            //  각 index에 대한 최소값 구하기
            for (int j = 0; j < n; j++){

                while ( tmp > subtractIndex[j]) {
                    tmp = subtractIndex[j];
                }
            }
            // intArr에 할당
            intArr[i] = tmp;
            
        }

        for (int x : intArr) {
            
        System.out.print(x + " ");
        }

      
        sc.close();
    }
    
}
