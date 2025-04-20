// HashSet 이용
// 메모리 초과
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class SetHash {
    public static void main(String args[]) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader((System.in)));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        // 명령어 개수
        int m = Integer.parseInt(reader.readLine().trim());

        // 집합
        HashSet<Integer> s = new HashSet<>();

        for (int i = 0; i < m; i ++) {
            String cmd = reader.readLine().trim();
            String[] cmdData = cmd.split(" ");

            String op = cmdData[0];
            if (cmdData.length > 1) {
                int num = Integer.parseInt(cmdData[1]);
                switch(op) {
                    case "add":
                        s.add(num);
                        break;
                    case "remove":
                        s.remove(num);
                        break;
                    case "check":
                        if (s.contains(num)) {
                            writer.write("1\n");
                        } else {
                            writer.write("0\n");
                        }
                        break;
                    case "toggle":
                        if (s.contains(num)) {
                            s.remove(num);
                        } else {
                            s.add(num);
                        }
                        break;
                }
            } else {
                switch(op) {
                    case "all":
                        s.clear();
                        for (int j = 1; j < m; j++) {
                            s.add(j);
                        }
                        break;
                    case "empty":
                        s.clear();
                        break;
                }
            }
        }

        // 버퍼 플러시
        writer.flush();
        writer.close();
        reader.close();
    }
}