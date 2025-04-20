import java.util.Scanner;
import java.util.HashMap;

public class president {

    public char solution(int n, char[] arr ) {

        char answer = 0;
        int max = Integer.MIN_VALUE;

        HashMap<Character,Integer> map = new HashMap<>();
        for (char x : arr) {
            // map에 x의 value 값이 있으면 가져오고, 아니면 0 +1으로 put
            // 키가 없을 때 사용하는 매우 중요한 map.getOrDefault()
            map.put(x, map.getOrDefault(x, 0) + 1);
        }

        // 키가 존재하는지 보는 거
        // System.out.println(map.containsKey('A'));

        // map의 크기(key의 개수)
        // System.out.println(map.size());

        // 특정 키 삭제하면서 그 특정키의 value값 return
        // System.out.println(map.remove('A'));

        // map 출력
        for (char key : map.keySet()) {
            // System.out.println(key + " " + map.get(key));
            if (map.get(key) > max) {
                max = map.get(key);
                answer = key;
            }
        }

        return answer;

    }

    public static void main(String args[]) {

        president T = new president();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String input = sc.next();

        char[] arr = input.toCharArray();
        System.out.println(T.solution(n,arr));
        sc.close();
    }
    
}
