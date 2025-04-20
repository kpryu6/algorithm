package sorting_searching.mischievous;

import java.util.*;

public class mischievous {

    public ArrayList<Integer> solution(int n, int[] arr) {

        ArrayList<Integer> answer = new ArrayList<>();
        // int[] arrCpy = arr.clone();
        int[] arrCpy = Arrays.copyOf(arr, n);
        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            if (arr[i] != arrCpy[i]) answer.add(i+1);
        }

        return answer;
    }

    
    public static void main(String args[]) {

        mischievous T = new mischievous();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int [n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (Integer x : T.solution(n,arr)) {
            System.out.print(x + " ");
        }
        
        sc.close();
    }
    
}
