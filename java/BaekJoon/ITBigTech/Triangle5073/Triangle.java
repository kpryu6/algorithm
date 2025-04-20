import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Triangle {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<int[]> inputs = new ArrayList<>();
        
        while (true) {
            // 문자열 양 끝 공백문자 제거
            String userInput = sc.nextLine().trim();
            if (userInput.equals("0 0 0")) {
                break;
            }

            String[] params = userInput.split(" ");
            if (params.length != 3) {
                System.out.println("한 줄에 3개의 파라미터가 필요합니다.");
                continue;
            }

            try {
                int a = Integer.parseInt(params[0]);
                int b = Integer.parseInt(params[1]);
                int c = Integer.parseInt(params[2]);

                // input 유효성 검사
                if (a > 0 && a <= 1000 && b > 0 && b <= 1000 && c > 0 && c <= 1000) {
                    inputs.add(new int[]{a,b,c});
                }
                else {
                    System.out.println("0 초과 1000 이하 여야함");
                }
            } 
            catch (NumberFormatException e) {
                System.out.println("모든 파라미터는 정수여야 함");
            }
        }

        for (int[] data : inputs) {
            int a = data[0];
            int b = data[1];
            int c = data[2];

            // 삼각형 유효성 검사
            if (a + b > c && b + c > a && a + c > b) {
                // 세 변 모두 같을 때
                if (a == b && b == c) {
                    System.out.println("Equilateral");
                }
                // 두 변이 같을 때
                else if (a == b || a == c || b == c) {
                    System.out.println("Isosceles");
                }
                else {
                    System.out.println("Scalene");
                }
            }
            else {
                System.out.println("Invalid");
            }
        }
        sc.close();
    }
}