
import java.util.*;

public class Kth_largest_number_inflearn {

    public int solution(int n, int k, int[] arr){
        int answer = -1;

        TreeSet<Integer> Tset = new TreeSet<>(Collections.reverseOrder());

        // i,j,l 모두 n까지로 해도됨
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int l = j + 1; l < n; l++) {
                    Tset.add(arr[i]+arr[j]+arr[l]);
                    // Tset.remove()
                    // Tset.first() -> 첫번째 꺼
                    // Tset.last() -> 마지막 꺼
                    // Tset.size()
                    // Set은 중복제거고, Tree는 정렬(이진트리)이다.
                }
            }
        }
        int cnt = 0;
        for (Integer x : Tset) {
            cnt++;
            if (cnt == k) return x;
        }
        return answer;

    }

    public static void main(String args[]){

        Kth_largest_number_inflearn T = new Kth_largest_number_inflearn();
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
