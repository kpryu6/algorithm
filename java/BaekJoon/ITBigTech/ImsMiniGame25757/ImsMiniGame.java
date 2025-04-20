import java.util.HashMap;
import java.util.Scanner;

public class ImsMiniGame {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String game = sc.next();

        HashMap<String, Integer> gameMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String name = sc.next();
            gameMap.put(name, 1);
        }

        if (game.equals("Y")) {
            System.out.println(gameMap.size());
        } else if (game.equals("F")) {
            System.out.println(gameMap.size() / 2);
        } else if (game.equals("O")) {
            System.out.println(gameMap.size() / 3);
        }
    }
}