import java.util.Scanner;

public class OlympicBest {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[][] countries = new int[N+1][3];

        int countryName; 

        for (int i = 0; i < N; i++) {
            countryName = sc.nextInt();
            countries[countryName][0] = sc.nextInt();
            countries[countryName][1] = sc.nextInt();
            countries[countryName][2] = sc.nextInt();
        }

        int answer = 1;
        for (int i = 1; i <= N; i++) {
            // 금메달 비교
            if (countries[i][0] > countries[K][0]) answer++;
            // 금,은메달 비교
            if (countries[i][0] == countries[K][0] && countries[i][1] > countries[K][1]) answer++;
            // 금,은,동메달 비교
            if (countries[i][0] == countries[K][0] && countries[i][1] == countries[K][1] && countries[i][2] > countries[K][2]) answer++;
        }

        System.out.println(answer);
        sc.close();
    }
    
}

