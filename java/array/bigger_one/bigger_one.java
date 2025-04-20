package array.bigger_one;

import java.util.Scanner;

public class bigger_one {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
    
        // N개
        int n = Integer.parseInt(sc.nextLine());
        // N개의 정수
        String[] str = sc.nextLine().split(" ");
        int[] answer = new int[n];
        
        for (int i = 0; i < n-1; i++) {

            // 뒤에가 크면
            if (Integer.parseInt(str[i]) < Integer.parseInt(str[i+1])) {

                answer[i] = (Integer.valueOf(str[i+1]));
            }
        }

        // 첫번째는 무조건 출력
        System.out.print(str[0]);

        // 나머지 출력
        for (int x : answer) {

            // 0이면 넘어가기
            if(x==0) continue;
            System.out.print(" " + x);
            
        }
        
        sc.close();

    }
    
}


// Integer.parseInt()는 int를 리턴
// Integer.valueOf()는 Integer 객체를 리턴