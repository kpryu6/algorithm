// �ϳ��ϳ� �� �ߴµ� �ٸ� ����� �����ٵ�..
package array.rock_scissor_paper;

// 1:����, 2:����, 3:��
import java.util.*;
public class rock_scissor_paper {

    public char[] solution(int n, int[] infoA, int[] infoB){

        char[] winner = new char[n];

        for (int i = 0; i < n; i++) {
            // ó���� A�� ��� �ʱ�ȭ
            winner[i] = 'A';

            // ��� ���
            if (infoA[i] == infoB[i]) winner[i] = 'D';

            // A�� ����
            else if (infoA[i] == 1) {

                if (infoB[i] == 2) winner[i] = 'B';
            }
            // A�� ����
            else if (infoA[i] == 2) {

                if (infoB[i] == 3) winner[i] = 'B';
            }
            // A�� ��
            else if (infoA[i] == 3) {

                if (infoB[i] == 1) winner[i] = 'B';
            }
            
        }

        return winner;

        
    }

    public static void main(String args[]) {

        rock_scissor_paper T = new rock_scissor_paper();
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
