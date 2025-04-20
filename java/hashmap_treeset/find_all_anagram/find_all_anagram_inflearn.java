import java.util.*;
public class find_all_anagram_inflearn {

    public int solution(String a, String b) {
        int answer = 0;

        HashMap<Character,Integer> am = new HashMap<>();
        HashMap<Character,Integer> bm = new HashMap<>();

        for (char x : b.toCharArray()) {
            bm.put(x,bm.getOrDefault(x, 0) + 1);
        }

        int lt = 0, L = b.length()-1;

        // b가 3일때 어디까지 먼저 put하고 갈거냐가 문제 : 여기선 2번째 까지했고 내가 푼거는 3번째 까지함
        for (int i = 0; i < L; i++) {
            am.put(a.charAt(i),am.getOrDefault(a.charAt(i), 0) + 1);
        }

        for (int rt = L; rt < a.length(); rt++) {
            // 그다음 것
            am.put(a.charAt(rt),am.getOrDefault(a.charAt(rt), 0) + 1);
            if (am.equals(bm)) answer++;

            // 뺄 것
            am.put(a.charAt(lt),am.getOrDefault(a.charAt(lt), 0) - 1);
            if (am.get(a.charAt(lt)) == 0) am.remove(a.charAt(lt));
            lt++;
        }



        return answer;

    }

    public static void main(String args[]) {

        find_all_anagram_inflearn T = new find_all_anagram_inflearn();
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        System.out.println(T.solution(a,b));
        sc.close();
    }
    
}
