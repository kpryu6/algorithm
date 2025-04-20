package hashmap_treeset.types_of_revenue;

import java.util.*;

public class types_of_revenue {

    public ArrayList<Integer> solution(int n, int k, int[] arr) {

        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Integer,Integer> map = new HashMap<>();
        int lt=0, rt = k-1;

        // k-1번 까지 먼저 저장
        for (int i = 0; i < rt; i++) {
            map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        }

        for (int i = rt; i < n; i++) {
            // k번째 저장
            map.put(arr[i],map.getOrDefault(arr[i], 0)+1);

            // 첫번째 k개의 key수
            answer.add(map.size());

            // 지나친 lt의 key가 있으면(당연히 있는거라 contains 안해도됨) value 하나 줄여주기
            if (map.containsKey(arr[lt])) {
                map.put(arr[lt], map.get(arr[lt]) -1);
                // value가 0이면 삭제
                if (map.get(arr[lt]) == 0) map.remove(arr[lt]);
            }
            lt++;
            /* 
            for (Integer key : map.keySet()) {
                System.out.println(key + " " + map.get(key));
            }
            System.out.println();
            */
            
        }
        return answer;
    }

    public static void main(String args[]) {

        types_of_revenue T = new types_of_revenue();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        for (Integer x : T.solution(n, k, arr)) {
            System.out.print(x+ " ");
        }
        
        sc.close();
    
    }
    
}


// 하.. Python이랑 헷갈려서 ArrayList append하다가 엥 왜안되지 했음;;
// ArrayList는 add!!!!!!