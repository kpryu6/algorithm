package string.cipher;

import java.util.Scanner;

class Main {
    public String solution(int n, String s) {

        String answer = "";

        for (int i = 0; i < n; i++) {
            // substring으로 짜르고 바로 replace로 바꿔주기
            String tmp = s.substring(0, 7).replace('#', '1').replace('*', '0');
            // 2진수로 넘어가는 tmp를 parseInt
            int num = Integer.parseInt(tmp, 2);
            // num을 char로 바꾸기
            answer += (char) num;
            // 자른 지점부터 끝까지(나머지) 할당
            s = s.substring(7);
        }

        return answer;
    }

}

public class cipher_easy {

    public static void main(String args[]) {

        Main T = new Main();

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();

        System.out.println(T.solution(n, str));

        sc.close();
    }
    
}
