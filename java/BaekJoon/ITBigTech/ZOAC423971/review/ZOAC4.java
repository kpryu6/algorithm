import java.util.Scanner;

public class ZOAC4 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String userInput = sc.nextLine().trim();
        String[] splits = userInput.split(" ");

        if (splits.length != 4) {
            System.out.println("파라미터는 4개가 필요합니다.");
            sc.close();
            return;
        }

        try {
            int H = Integer.parseInt(splits[0]);
            int W = Integer.parseInt(splits[1]);
            int N = Integer.parseInt(splits[2]);
            int M = Integer.parseInt(splits[3]);

            if (H > 0 && H <= 50000 && W > 0 && W <= 50000 && N > 0 && N <= 50000 && M > 0 && M <= 50000) {
                int checkRows = ((H - 1) / (N + 1)) + 1;
                int checkCols = ((W - 1) / (M + 1)) + 1;
                System.out.println(checkRows * checkCols);
            }

        } catch (NumberFormatException e) {
            System.out.println("파라미터는 정수여야 합니다");
        }
        sc.close();
    }
}