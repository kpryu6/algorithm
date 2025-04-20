import java.util.*;

public class duplication_check {

    public char solution(int n, int[] arr) {
        char answer = 'D';

        HashSet<Integer> hashSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            hashSet.add(arr[i]);
        }
        if (hashSet.size() == n) return 'U';


        return answer;

    }

    public static void main(String args[]) {

        duplication_check T = new duplication_check();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(n,arr));
        sc.close();

    }
    
}
