

// 올바른 중복 제거 로직을 구현하기 위해 StringBuilder를 사용
package string.delete_duplicated_word;

import java.util.Scanner;

public class delete_duplicated_word {

    public static void main (String args[]) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        // String은 불변 클래스이기 때문에 문자조작에는 StringBuilder 쓰기
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {

            char currentChar = str.charAt(i);

            // sb에 currentChar이 없으면
            if (sb.indexOf(String.valueOf(currentChar)) == -1) {
                
                sb.append(currentChar);
                
            }
        }
        
        String answer = sb.toString();
        System.out.println(answer);

        sc.close();
    }
    
}

// indexOf는 문자열에서 해당 문자를 검색할 때 첫번째로 발견되는 index를 리턴
// str = "goog" -> str.indexOf('g') -> 0