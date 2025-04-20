package string.flip_over_word;

import java.util.Scanner;

public class flip_over_word_1 {

    public static void main (String args []) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 받은 단어들 한번에 배열로 만들 수 있었다..
        String [] str = new String[n];

        for (int i = 0; i < n; i++) {
            str[i] = sc.next(); // 공백 문자 만나면 그 앞까지 받아옴
        }

        // ** NEW ** //
        // StringBuilder를 이용해 객체 생성 제한
        for (String x : str) {
            String wordReverse = new StringBuilder(x).reverse().toString();
            System.out.println(wordReverse);
        }
        
        sc.close();

    }
    
}
