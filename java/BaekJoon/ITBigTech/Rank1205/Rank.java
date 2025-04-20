import java.util.*;
import java.io.*;

public class Rank {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int newScore = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        
        int[] rankList = new int[N];
        
        if (N > 0) {
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < N; i++) {
                rankList[i] = Integer.parseInt(st2.nextToken());
            }
        }

        int rank = 1;
        
        for (int i = 0; i < N; i++) {
            if (newScore > rankList[i]) break;
            else if (newScore == rankList[i]) break;
            else rank++;
        }

        if (N > 0 && N == P && newScore <= rankList[N-1]) System.out.println(-1);
        else System.out.println(rank);
    }
}

