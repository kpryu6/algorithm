import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudyWord {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String userInput = sc.next().toUpperCase();

        // System.out.println(userInput);

        HashMap<Character,Integer> freqMap = new HashMap<>();

        // freqMap에 해당 key 빈도수 추가
        for (char word : userInput.toCharArray()) {
            freqMap.put(word, freqMap.getOrDefault(word,0) + 1);
        }

        // System.out.println(freqMap);

        // 최대 빈도수 계산
        int maxFreq = 0;
        for (int freq : freqMap.values()) {
            if (freq > maxFreq) {
                maxFreq = freq;
            }
        }

        // System.out.println(freqMap.entrySet());

        int maxFreqCount = 0;
        char maxFreqWord = '?';

        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            if (entry.getValue() == maxFreq) {
                maxFreqCount++;
                maxFreqWord = entry.getKey();
            }
        }

        if (maxFreqCount > 1) {
            System.out.println('?');
        }
        else {
            System.out.println(maxFreqWord);
        }
        sc.close();
    }
}