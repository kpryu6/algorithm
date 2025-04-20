package string.flip_over_word;

import java.util.Scanner;

public class flip_over_word_2 {

    public static void main (String args []) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 받은 단어들 한번에 배열로 만들 수 있었다..
        String [] str = new String[n];

        for (int i = 0; i < n; i++) {
            str[i] = sc.next(); // 공백 문자 만나면 그 앞까지 받아옴
        }

        // ** NEW ** //
        // 직접 자리 바꾸기 toCharArray 사용
        for (String x : str) {
            char [] charArray = x.toCharArray();
            int left = 0;
            int right = x.length()-1;
            while (left < right) { // study의 경우
                char tmp = charArray[left]; // tmp = s
                charArray[left] = charArray[right]; // ytudy
                charArray[right] = tmp; // ytuds
                left++;
                right--;
            }
            String answer = String.valueOf(charArray);
            System.out.println(answer);
        }
        sc.close();

    }
    
}

/*
1) StringBuilder

예를 들어 String 객체 두개를 더하면 새로운 객체가 생성되어 객체가 3개가 된다. 객체의 무한생성을 제한하기 위해 쓰며 출력을 할 경우 toString()을 쓴다.

?

2) valueOf()

String tmp = String.valueOf(s);
char s를 String으로 바꾸어 tmp에 저장
지정 값을 문자열로 변환 후 반환


3)StringBuilder.reverse()

문자를 하나 더 만들지않고 그대로 리버스

 */
