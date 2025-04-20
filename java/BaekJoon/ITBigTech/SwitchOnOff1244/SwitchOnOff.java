import java.util.*;
import java.io.*;

public class SwitchOnOff {

    public static void toggle(int[] switchList, int k) {
        if (switchList[k] == 1) switchList[k] = 0;
        else if (switchList[k] == 0) switchList[k] = 1;
    }

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 한줄 String 토큰화 하는거임
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim()); // 스위치 개수
        
        int[] switchList = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            switchList[i] = Integer.parseInt(st.nextToken());
        }

        int peopleLen = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < peopleLen; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            
            // male
            if (gender == 1) {
                for (int j = 0; j < N; j++) {
                    if ((j+1) % num == 0){ 
                        toggle(switchList, j);        
                    }
                }
            }
            // female
            else if (gender == 2){
                num = num - 1;
                toggle(switchList, num);
                int left = num - 1;
                int right = num + 1;
                
                while ((left >= 0) && (right < N) && (switchList[left] == switchList[right])) {
                    toggle(switchList, left);
                    toggle(switchList, right);
                    left = left - 1;
                    right = right + 1;
                }
            }
        }
        // print
        for (int i = 0; i < N; i++) {
            System.out.print(switchList[i] + " ");
            if ((i+1) % 20 == 0) {
                System.out.println();
            }
        }
        if (N <= 20) System.out.println();
    }
}
