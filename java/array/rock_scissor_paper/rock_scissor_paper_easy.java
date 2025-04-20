// 하나하나 다 했는데 다른 방법이 있을텐데..
package array.rock_scissor_paper;

// 1:가위, 2:바위, 3:보
import java.util.*;
public class rock_scissor_paper_easy {

    public char[] solution(int n, int[] A, int[] B){

        char[] winner = new char[n];

        for (int i = 0; i < n; i++) {
           
            // 코드 줄이기
            if (A[i] == B[i]) winner[i] = 'D';
            else if (A[i] == 1 && B[i] == 3) winner[i] = 'A';
            else if (A[i] == 2 && B[i] == 1) winner[i] = 'A';
            else if (A[i] == 3 && B[i] == 2) winner[i] = 'A';
            else winner[i] = 'B';
            
        }

        return winner;

        
    }

    public static void main(String args[]) {

        rock_scissor_paper_easy T = new rock_scissor_paper_easy();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] infoA = new int[n];
        int[] infoB = new int[n];

        for (int i = 0; i < n; i++) {
            infoA[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            infoB[i] = sc.nextInt();
        }

        for (char x : T.solution(n,infoA,infoB)){
            System.out.println(x);
        }
        
        sc.close();
    }
    
}
