
//time limit exceeded
package hashmap_treeset.types_of_revenue;

import java.util.*;

public class types_of_revenue_time_limit_exceeded {

    public int[] solution(int n, int k, int[] arr) {

        int[] answer = new int[n-k+1];
        HashMap<Integer,Integer> map = new HashMap<>();

        int j = 0;
        while (j < n-k+1){

            for (int i = j; i < k + j; i++) {
                map.put(arr[i],map.getOrDefault(arr[i],0)+1);
            }
            answer[j] = map.size();
            map.clear();
            j++;
        }
        return answer;

    }

    public static void main(String args[]) {

        types_of_revenue_time_limit_exceeded T = new types_of_revenue_time_limit_exceeded();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < n-k+1; i++) {
            System.out.print(T.solution(n,k,arr)[i]+ " ");
        }
        sc.close();
    
    }
    
}
