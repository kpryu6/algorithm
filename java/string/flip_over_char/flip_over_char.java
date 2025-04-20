package string.flip_over_char;

import java.util.Scanner;

public class flip_over_char {

    public static void main (String args[]) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        String answer = "";

        char [] charArray = str.toCharArray();

        int left = 0;
        int right = str.length() -1;

        while(left<right) {

            // 맨 왼쪽이 Alphabet이 아니면
            if(!Character.isAlphabetic(charArray[left])) left++;
            
            // 맨 오른쪽이 Alphabet이 아니면
            else if (!Character.isAlphabetic(charArray[right])) right--;

            // 둘다 Alphabet 이면
            else {
                char tmp = charArray[left];
                charArray[left] = charArray[right];
                charArray[right] = tmp;
                left++;
                right--;
            } 
        }

        answer = String.valueOf(charArray);

        System.out.println(answer);

        sc.close();


    }


    
}

// 1) Character.isAlphabetic(char ch)??
// ch가 알파벳이면 1 리턴 