package string.case_conversion;

import java.util.Scanner;

public class case_conversion {
    
    public static void main(String[] args) {

        // 입력받은 문자열을 바꿀 생각도 좋지만 새로 만들어서 넣는 것도 생각하기
        String answer = "";

        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        char [] strArray = str.toCharArray();

        for (char x : strArray) {
            
            // if (x>=97 && x<=122)
            if (Character.isLowerCase(x)) {
                answer += Character.toUpperCase(x);
            }
            else answer += Character.toLowerCase(x);

        }

        System.out.println(answer);
        sc.close();

    }
}

/* 
 * Character.isLowerCase(char ch) -> 소문자니? 알려주는 메소드
 * ASKII 코드로 대문자는 65~90 소문자는 97~122 -> 소문자 -32 = 대문자
 */
