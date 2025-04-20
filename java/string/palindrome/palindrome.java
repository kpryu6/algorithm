package string.palindrome;

import java.util.Scanner;

public class palindrome {

    public static void main( String args[]) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        // 대소문자 구분 안하므로 전체를 대문자로 해주기
        char[] charArray = str.toUpperCase().toCharArray();

        int left = 0;
        int right = str.length() - 1;
        
        while(left < right) {

            // left 문자와 right 문자가 같으면
            if ((charArray[left] == charArray[right])) {
                left++;
                right--;
            }

            else {
                System.out.println("NO"); 
                break;
            }
         }
            
        if ((left >= right)) System.out.println("YES");
        sc.close();

    }
    
}
