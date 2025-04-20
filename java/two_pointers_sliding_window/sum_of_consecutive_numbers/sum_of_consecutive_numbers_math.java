
// 수학적 방법
// 만약 15를 7+8 처럼 2개로 나눈다고 하자.
// 하나에는 1을, 다른 하나에는 2를 할당하자. (연속된 자연수)
// 15 - (1 + 2) = 12
// 12를 그 2개로 나눠서 정학히 떨어지면 그 몫을 1과 2에 더한다
// 1+6 = 7, 2+6 = 8

package two_pointers_sliding_window.sum_of_consecutive_numbers;

import java.util.Scanner;

public class sum_of_consecutive_numbers_math {

    public int solution(int n){
        // cnt : 몇개로 나누냐
        int answer = 0, cnt = 1;
        n--;

        while (n>0) {
            cnt++;
            n = n - cnt;
            if (n%cnt == 0) answer++;
        }

        return answer;
    }

    public static void main(String args[]) {

        sum_of_consecutive_numbers_math T = new sum_of_consecutive_numbers_math();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(T.solution(n));
        sc.close();
    }
    
}
