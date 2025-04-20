
// me

package string.flip_over_word;

import java.util.Scanner;

public class flip_over_word {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        String sentence = "";

        for (int i = 0; i<num; i++) {
            String word = sc.nextLine();
            sentence += word + " ";
        }

        // sentence에 있는 단어들 공백으로 분리해서 wordArray 만들기
        String [] wordArray = sentence.split(" "); 


        for (String word : wordArray) {

            String reverseWord= "";

            for (int i = word.length()-1 ; i>=0; i--) {

                reverseWord += word.charAt(i);
            }

            System.out.println(reverseWord);
        }
        sc.close();

    }
}