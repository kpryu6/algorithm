import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudyWord {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        char[] userInput = sc.next().trim().toUpperCase().toCharArray();
        HashMap <Character, Integer> map = new HashMap<>();

        for (char word : userInput) {
            // getOrDefault : word가 있으면 word의 value, word 없으면 null 대신 기본값 반환
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        
        int max = 0;
        for (int freq : map.values()) {
            if (freq > max) max = freq;
        }
        
        int maxCount = 0;
        char maxWord = '?';
        
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                maxCount++;
                maxWord = entry.getKey();
            }
        }

        if (maxCount > 1) System.out.println('?');
        else System.out.println(maxWord);
        sc.close();
    }
}