

// 이거 오답임!!!!!!!! (This code is error)

package string.delete_duplicated_word;

import java.util.Scanner;

public class delete_duplicated_word_ERROR {

    public static void main( String args [] ) {

        Scanner sc = new Scanner(System.in);

        // 입력받은 문자열
        String str = sc.next();

        // 문자열 문자배열로 만들기
        char[] charArray = str.toCharArray();

        for (char x : charArray) {

            // x 다음부터 끝까지 x랑 같은 글자 찾아서 제거
            for (int i = str.indexOf(x) + 1; i < str.length(); i++) {
                
                if (x == charArray[i]) {
                    
                    // ** 이렇게 하면 제거하는게 아니고 null값으로 바꿔주는거라 오류 **
                    charArray[i] = '\0';

                }
            }
            
        }

        for (int i = 0; i < charArray.length; i++){
            System.out.println(charArray[i]);
        }

        
        sc.close();
        

    }
    
}
