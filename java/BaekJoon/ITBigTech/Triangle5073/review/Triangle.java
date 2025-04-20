import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Triangle {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        List<int[]> list = new ArrayList<>();

        while(true) {
            String userInput = sc.nextLine().trim();
            if (userInput.equals("0 0 0")) {
                break;
            }

            String[] splits = userInput.split(" ");
            if (splits.length != 3) {
                System.out.println("파라미터는 3개여야 합니다.");
            }

            boolean valid = true;
   
            for (String split : splits) {
                int value = Integer.parseInt(split);
                if (value < 0 && value >= 1000) {
                    System.out.println("1000 이하의 양의 정수여야 합니다.");
                    valid = false;
                    break;
                } 
            }

            int d = Integer.parseInt(splits[0]);
            int e = Integer.parseInt(splits[1]);
            int f = Integer.parseInt(splits[2]);

            if (valid) {
                list.add(new int[]{d,e,f});
            }
        }
        for (int[] data : list) {
            int a = data[0];
            int b = data[1];
            int c = data[2];

            // 삼각형 유효성 검사
            if (a + b > c && a + c > b && b + c > a) {
                // 세 변이 같을 때
                if (a == b && b == c) {
                    System.out.println("Equilateral");
                }
                // 두 변이 같을 때
                else if (a == b || a == c || b == c) {
                    System.out.println("Isosceles");
                } else {
                    System.out.println("Scalene");
                }
            } else {
                System.out.println("Invalid");
            }
        }

        sc.close();
    }
}