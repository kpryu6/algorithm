
import java.util.*;

public class Kth_largest_number {

    public int solution(int n, int k, int[] arr){
        int answer = 0;

        HashMap<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int l = j + 1; l < n; l++) {
                    map.put(arr[i]+arr[j]+arr[l],map.getOrDefault(arr[i]+arr[j]+arr[l], 0) + 1);
                }
            }
        }
        for (int i = 0; i < k; i++) {
            int max = 0;
            for (Integer x : map.keySet()) {
                if (max < x) {
                    max = x;
                }
            }
            if (i == k - 1) {
                answer = max; 
                break;
            }
            // k번째 수가 존재하지 않으면 -1
            if (k > n) return -1;
             map.remove(max);
        }
        return answer;

    }

    public static void main(String args[]){

        Kth_largest_number T = new Kth_largest_number();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(n,k,arr));
        sc.close();
    }
    
}
