package string.word_in_sentence;

import java.util.Scanner;

public class word_in_sentence1 {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        String answer = "";

        int m = 0;
        // index를 잡아서 끊어보자
        int pos;
        // pos가 공백을 발견 못하면 -1 리턴
        // * 마지막 단어 뒤엔 공백이 없으니 마지막 단어도 작업해주기
        while ((pos = str.indexOf(" ")) != -1) {

            String word = str.substring(0, pos);
            int len = word.length();

            if (len > m) { //len >= m 하면 같은 길이의 단어 중 뒤에 단어가 답이됨
                m = len;
                answer = word;
            }

            str = str.substring(pos+1);
            
        }
        // * 마지막 단어
        if (str.length() > m) answer = str;

        System.out.println(answer);
        sc.close();

    }
    
}

/*

2) indexOf(String str)

int pos = str.indexOf(" ");

문자열의 공백의 index 값을 할당

?

3) substring(int a, int b)

String word = str.substring(0,pos);

str의 인덱스 a부터 b까지를 word에 할당

--> substring(int a) 하면 str의 인덱스 a부터 끝까지 word에 할당
 */