import java.util.*;

// 결정 알고리즘
// 특정 범위 내에 무조건 답이 있다

// Scanner에 문제가 있나.. 입력을 무한으로 받음 -> 해결
public class music_video {

    public boolean canAnswer (int n, int m, int[] arr, int mid) {
        
        int sum = 0;
        int count = 1;
        boolean answer = true;

        for (int i = 0; i < n; i++) {
            if (sum + arr[i] > mid) {
                count++;
                sum = arr[i];
            }
            else sum += arr[i];
        }

        if (count > m) answer = false;
            
        return answer;
        
    }

    public int solution (int n, int m, int[] arr) {
        // lt : arr의 최대 값 (한장에 들어갈 수 있는 최소값)
        // rt : arr 합 (한장에 들어갈 수 있는 최대값)
        int answer = 0;
        // max() 까지 하면 OptionalInt 여서 형변환
        int lt = Arrays.stream(arr).max().getAsInt();
        // Arrays.stream(arr) 는 IntStream (int형 요소를 가지는 스트림)
        int rt = Arrays.stream(arr).sum();
        for (int i = 0; i < n; i++) rt += arr[i];

        while (lt <= rt) {

            int mid = (lt + rt)/2;
            // if (lt == rt) answer = mid;
            // 이거 때문에 Scanner 무한루프 돌았음
            // 밑에 if문과 겹쳐서!
            if (canAnswer(n, m, arr, mid)) {
                answer = mid;
                rt = mid - 1;
            }
            else lt = mid + 1;

        }
        return answer;
    }

    public static void main(String args[]) {

        music_video T = new music_video();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(n,m,arr));
        sc.close();
    }
    
}

// 이분 검색은 계속 하다보면 lt가 rt보다 커진다