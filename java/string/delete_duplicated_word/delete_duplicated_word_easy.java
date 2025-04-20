package string.delete_duplicated_word;

import java.util.Scanner;

public class delete_duplicated_word_easy {

    public static void main (String args[]) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        String answer = "";

        for (int i = 0; i < str.length(); i++) {

            // i == str.indexOf(str.charAt(i)) 이면 중복문자는 저절로 제거됨
            if (i == str.indexOf(str.charAt(i))) answer += str.charAt(i);

        }

        System.out.println(answer);
        sc.close();


    }
    
}
