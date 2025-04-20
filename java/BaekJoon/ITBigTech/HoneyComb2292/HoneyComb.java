import java.util.Scanner;
public class HoneyComb {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();

        int n = 1;
        while(true) {
            if (k == 1) {
                break;
            }
            else if (3 * n * n + 3 * n + 1 >= k) {
                n++;
                break;
            }
            n++;
        }
        System.out.println(n);
        sc.close();
    }
    
}
