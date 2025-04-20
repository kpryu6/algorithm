import java.util.Scanner;

public class LineUp {

    public static int bubbleSort(int[] list) {
        int steps = 0;
        // 끝에서부터 고정시키는 것
        for (int i = list.length - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (list[j] > list[j+1]) {
                    int tmp = list[j];
                    list[j] = list[j+1];
                    list[j+1] = tmp;
                    steps++;
                }
            }
        }
        return steps;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int P = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < P; i++) {
            String[] splits = sc.nextLine().split(" ");
            int N = Integer.parseInt(splits[0]);
            int[] x = new int[splits.length - 1];

            for (int j = 1; j < splits.length; j++) {
                x[j - 1] = Integer.parseInt(splits[j]);
            }

            System.out.println(N + " " + bubbleSort(x));
        }
    }
}
