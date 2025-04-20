import java.util.*;

public class music_video_inflearn {

    public int count (int[] arr, int capacity) {
        
        int cnt = 1, sum = 0;
        for (int x : arr) {
            if (sum + x > capacity) {
                cnt++;
                sum = x;
            }
            else sum += x;
        }
        return cnt;
        
    }

    public int solution (int n, int m, int[] arr) {

        int answer = 0;
        int lt = Arrays.stream(arr).max().getAsInt();
        int rt = Arrays.stream(arr).sum();

        while (lt <= rt) {
            int mid = (lt+rt)/2;
            if (count(arr, mid) <= m) {
                answer = mid;
                rt = mid - 1;
            }
            else lt = mid + 1;
        }
        return answer;

    }

    public static void main(String args[]) {

        music_video_inflearn T = new music_video_inflearn();
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

// stream()
// 컬렉션(Collection)과 배열(Array) 등의 데이터 소스를 함수형 프로그래밍 방식으로 처리할 수 있도록 해줌

