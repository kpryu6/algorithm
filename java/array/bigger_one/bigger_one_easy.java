package array.bigger_one;

import java.util.*;

class Main {
    public ArrayList<Integer> solution(int n, int[] arr) {

        ArrayList<Integer> answer = new ArrayList<>();

        // 첫번째는 무조건 들어감
        answer.add(arr[0]);
        for (int i = 0; i < n - 1; i++) {

            if (arr[i] < arr[i+1]) answer.add(arr[i+1]);
        }
        return answer;

    }
}

public class bigger_one_easy {

    public static void main(String args[]) {

        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];

        // 입력하자마자 배열로 넣었네
        for (int i = 0; i < n; i++) {

            arr[i] = sc.nextInt();

        }

        for(int x : T.solution(n,arr)) {

            System.out.print(x+ " ");

        }
        sc.close();

    }
    
}
