//fn + f5로 compile

package string.find_word;

import java.util.Scanner;

public class find_word {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char ch = sc.next().charAt(0);

        // 특정 word를 찾기 위해 입력받은 (문자열 & 문자) 대문자로 바꾸기
        String upperStr = str.toUpperCase();
        char upperCh = Character.toUpperCase(ch); // ** 문자를 대문자로 바꿔줌 **

        int answer = 0;
        
        // upperStr을 배열로 만들어주기
        for (char x : upperStr.toCharArray()) {

            if (x == upperCh) answer ++;
        }

        System.out.println(answer);

        sc.close();
    }
}

    /*  
    * charAt(int index) -> 문자열에서 인덱스의 값의 문자를 꺼내옴
    * toCharArray() -> 문자열을 배열로 만들어줌
    * Character.toUpperCase(char ch) -> 문자를 대문자로바꿔줌 // 메소드 만들 필요없음.
    */
    
