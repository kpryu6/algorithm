
import java.util.*;

class Person {
    int id;
    int priority;
    public Person (int id, int priority) {
        this.id = id;
        this.priority = priority;
    }
}

public class emergency {

    public int solution (int n, int m, int[] arr) {
        int answer = 0;

        Queue<Person> Q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            Q.offer(new Person(i, arr[i]));
        }

        while (!Q.isEmpty()) {
            // 일단 하나 뽑아
            Person p = Q.poll();
            // 돌면서 위험도 비교
            for (Person x : Q) {
                if (x.priority > p.priority) {
                    Q.offer(p);
                    p = null;
                    break;
                }
            }
            if (p != null) {
                answer++;
                if (p.id == m) return answer;
            }
        }
        return answer;

    }

    public static void main(String args[]){

        emergency T = new emergency();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(n,m,arr));
        sc.close();
    }
    
}
