package array.visible_student;

import java.util.*;


public class visible_student {

    public int solution(int n, int[] arr){
        
        int answer = 0;
        int max = Integer.MIN_VALUE;

        // 148을 max로 어떻게 고정하지?
        // 현재 index 왔을 때 * 앞에 애들 다 검사해서* 자기보다 큰거 있으면 안보이는거고 자기보다 다 작으면 자기 보이는거고
        outerLoop:
        for (int i = 0; i < n; i++) {

            max = arr[i];

            for (int j = 0; j < i; j++) {
                // 앞에 있는 것들중에 어떤 것이 더 큰 경우
                if (max <= arr[j]){
                    max = arr[j];
                    // 앞에 하나라도 크면 안보이니까 그냥 바로 continue
                    continue outerLoop;
                }
                // 자기가 젤 큰 경우라서 아무 문제없음
            }

            // for문에 continue 있으니 문제 없을 경우만 answer 증가
            answer++;

        }

        return answer;
    }


    public static void main(String args[]){

        visible_student T = new visible_student();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] heights = new int[n];

        for(int i = 0; i < n; i++) {

            heights[i] = sc.nextInt();
        
        }
        System.out.println(T.solution(n,heights));
        sc.close();
    
    }

   
}
