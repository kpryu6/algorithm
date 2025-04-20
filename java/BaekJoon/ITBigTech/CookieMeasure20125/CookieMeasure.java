import java.util.*;

public class CookieMeasure {
    public static void main(String args[]){
	    Scanner sc = new Scanner(System.in);	
        int N = Integer.parseInt(sc.nextLine().trim());

        ArrayList<String> rows = new ArrayList<>();

        // 입력 저장
        for (int i = 0; i < N; i++) {
            rows.add(sc.nextLine());
        }

        // 머리 저장
        int[] head = new int[2];
        for (int i = 0; i < N; i++) {
            if (rows.get(i).contains("*")) {
                head[0] = i+2;
                head[1] = rows.get(i).indexOf("*") + 1;
                break;
            }
        }

        // 몸
        int leftHand = 0, rightHand = 0, waist = 0, leftLeg = 0, rightLeg = 0;
        
        for (int i = head[0] - 1; i < N; i++) {

            // 팔
            if (i == head[0] - 1) {
                // 왼팔
                for (int j = 0; j < head[1]-1; j++) {
                    if (rows.get(i).charAt(j) == '*') {
                        leftHand++;
                    }
                }
                // 오른팔
                for (int j = head[1]; j < rows.get(i).length(); j++) {
                    if (rows.get(i).charAt(j) == '*') {
                        rightHand++;
                    }
                }
            }

            if (i >= head[0]) {
                // 허리
                if (rows.get(i).charAt(head[1]-1) == '*') waist++;

                // 다리
                if (rows.get(i).charAt(head[1]-2) == '*' && rows.get(i).charAt(head[1]) == '*') {
                    leftLeg++;
                    rightLeg++;
                } else if (rows.get(i).charAt(head[1]-2) == '*') leftLeg++;
                else if (rows.get(i).charAt(head[1]) == '*') rightLeg++;
            }
        }

        System.out.printf("%s %s\n", head[0], head[1]);
        System.out.printf("%d %d %d %d %d\n", leftHand, rightHand, waist, leftLeg, rightLeg);
        sc.close();
    }
}

