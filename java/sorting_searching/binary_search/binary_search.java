package sorting_searching.binary_search;

import java.util.*;

public class binary_search {

    public int solution (int n, int m, int[] arr) {
        int answer = 0, lt = 0, rt = n-1;

        Arrays.sort(arr);

        while (lt <= rt) {
            int mid = (lt+rt)/2;
            
            if (m == arr[mid]) {
                answer = mid+1;
                break;
            }
            else if (m > arr[mid]) lt = mid + 1;
            else if (m < arr[mid]) rt = mid - 1;

        }

        return answer;

        }
    

    public static void main (String args[]) {

        binary_search T = new binary_search();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr =  new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(T.solution(n, m, arr));
        sc.close();

    }
    
}
