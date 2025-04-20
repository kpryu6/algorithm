import java.util.*;

public class anagram {

    public String solution (String a, String b) {
        
        HashMap<Character,Integer> map = new HashMap<>();
        for (char key : a.toCharArray()) {
            map.put(key,map.getOrDefault(key, 0)+1);
        }
        HashMap<Character,Integer> map1 = new HashMap<>();
        for (char key : b.toCharArray()) {
            map1.put(key,map1.getOrDefault(key, 0)+1);
        }
        
        for (char key : map.keySet()) {
            // map1에 map의 key가 들어있으면
            if (map1.containsKey(key) && map1.containsValue(map.get(key))) continue;
            
            else return "NO";
        }
        return "YES";
    }

    public static void main(String args[]) {

        anagram T = new anagram();
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();
        System.out.println(T.solution(str1,str2));
        sc.close();
    }
    
}
