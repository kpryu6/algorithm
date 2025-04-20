import java.util.*;

public class find_all_anagram {

    public int solution(String T, String S) {
        int answer = 0;
    
        // S의 Hashmap
        HashMap<Character,Integer> Smap = new HashMap<>();
        for (char c : S.toCharArray()) {
            Smap.put(c,Smap.getOrDefault(c, 0)+1);
        }
    
        // T의 Hashmap
        HashMap<Character,Integer> Tmap = new HashMap<>();
        char[] Tarr = T.toCharArray();
        int lt = 0, rt = S.length();
    
        // rt까지 일단 Hashmap에 저장 (Sliding Window)
        for (int i = 0; i < rt; i++) {
            Tmap.put(Tarr[i],Tmap.getOrDefault(Tarr[i], 0)+1);
        }
    
        while (rt <= T.length()){
            // equals로 하기
            // entrySet() 메소드는 Map의 키(key)와 값(value)을 모두 포함하는 Entry 객체의 집합(set)을 반환
            if (Tmap.entrySet().equals(Smap.entrySet())) {
                answer++;
            }
            if (rt == T.length()) break;
            // 다음인덱스 +, 젤 작은 인덱스 -
            Tmap.put(Tarr[rt],Tmap.getOrDefault(Tarr[rt],0)+1);
    
            Tmap.put(Tarr[lt], Tmap.get(Tarr[lt]) - 1);
            if (Tmap.get(Tarr[lt]) == 0) Tmap.remove(Tarr[lt]);
            lt++;
            rt++;
        }
            
        return answer;
    }
    


    public static void main(String args[]) {

        find_all_anagram m = new find_all_anagram();
        Scanner sc = new Scanner(System.in);
        String T = sc.next();
        String S = sc.next();

        System.out.println(m.solution(T,S));
        sc.close();
    }
    
}
