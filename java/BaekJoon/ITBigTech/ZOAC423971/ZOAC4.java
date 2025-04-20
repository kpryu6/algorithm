import java.util.Scanner;

public class ZOAC4 {
    public static void main(String[] args) {
        // System.out.println("ZOAC4");
        Scanner sc = new Scanner(System.in);
        String userInput = sc.nextLine();
        String[] pv = userInput.split(" ");

        if (pv.length != 4) {
            System.out.println("파라미터 4개 입력하세요");
            sc.close();
            return;
        }

        try {
            int H = Integer.parseInt(pv[0]);
            int W = Integer.parseInt(pv[1]);
            int N = Integer.parseInt(pv[2]);
            int M = Integer.parseInt(pv[3]);

            if (H > 0 && H <= 50000 && W > 0 && W <= 50000 && N > 0 && N <= 50000 && M > 0 && M <= 50000) {
                
                int checkRows = ((H - 1) / (N + 1)) + 1;
                int checkCols = ((W - 1) / (M + 1)) + 1;

                int answer = checkCols * checkRows;
                System.out.println(answer);
            }
            else {
                System.out.println("각 파라미터는 0 초과 50000 이하여야 함");
            }

        } catch (NumberFormatException e) {
            System.out.println("모든 파라미터는 정수여야 함");
        } 
        sc.close();
    }
}