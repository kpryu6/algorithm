import java.util.Scanner;

public class PWD {

    // 모음인가?
    public static boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }

    // 모음 존재 유무
    public static boolean contiansVowel(String input) {
        for (char c : input.toCharArray()) {
            // c가 aeiou 중에 있으면 true
            if ("aeiou".indexOf(c) != -1) {
                return true;
            }
        }
        return false;
    }

    // 모음이나 자음이 연속 3번 있는지
    public static boolean isTriple(String input) {
        for (int i = 0; i < input.length() - 2; i++) {
            // 모음 연속 3번
            if (isVowel(input.charAt(i)) && isVowel(input.charAt(i+1)) && isVowel(input.charAt(i+2))) {
                return true;
            }
            // 자음 연속 3번
            if (!isVowel(input.charAt(i)) && !isVowel(input.charAt(i+1)) && !isVowel(input.charAt(i+2))) {
                return true;
            }
        }
        return false;
    }

    // ee나 oo를 제외한 글자가 연속 2번 있는지
    public static boolean isDouble(String input) {
        for (int i = 0; i < input.length() - 1; i++) {
            if (input.charAt(i) == input.charAt(i+1) && input.charAt(i) != 'e' && input.charAt(i) != 'o') {
                return true;
            }
        }
        return false;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        while (true) {
            String input = sc.nextLine();
            if (input.equals("end")) break;

            boolean case1 = contiansVowel(input);
            boolean case2 = !isTriple(input);
            boolean case3 = !isDouble(input);

            if (case1 && case2 && case3) {
                System.out.println("<" + input + "> is acceptable.");
            } else {
                System.out.println("<" + input + "> is not acceptable.");
            }
        }
        sc.close();
    }
}
