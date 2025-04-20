
import java.util.*;

public class least_recently_used_inflearn {

    public int[] solution(int cacheSize, int workOut, int[] workOutArr) {

        int[] cache = new int[cacheSize];
        for (int x : workOutArr) {
            int pos = -1;
            // cache hit
            for (int i = 0; i < cacheSize; i++) if (x == cache[i]) pos = i;

            // cache miss
            if (pos == -1) {
                for (int i = cacheSize - 1; i >= 1; i--) {
                    cache[i] = cache[i-1];
                }
            }
            // cache hit
            else {
                for (int i = pos; i >= 1; i--) {
                    cache[i] = cache[i-1];
                }

            }
            
            cache[0] = x;

        }

       return cache;
    }

    public static void main(String args[]) {

        least_recently_used_inflearn T = new least_recently_used_inflearn();
        Scanner sc = new Scanner(System.in);
        int cacheSize = sc.nextInt();
        int workOut = sc.nextInt();
        int[] workOutArr = new int [workOut];

        for (int i = 0; i < workOut; i++) {
            workOutArr[i] = sc.nextInt();
        }

        for (int x : T.solution(cacheSize, workOut, workOutArr)) {
            System.out.print(x + " ");
        }
        sc.close();
    }
    
}
