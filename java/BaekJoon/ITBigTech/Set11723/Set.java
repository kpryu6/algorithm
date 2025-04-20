// BitMask 이용
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Set {
    public static void main(String args[]) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader((System.in)));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int s = 0;

        int m = Integer.parseInt(reader.readLine().trim());

        for (int i = 0; i < m; i++) {
            String cmd = reader.readLine().trim();
            String[] cmdData = cmd.split(" ");
            String op = cmdData[0];

            if (cmdData.length > 1) {
                int num = Integer.parseInt(cmdData[1]);

                switch(op) {
                    case "add":
                        // ex) 0001을 num만큼 왼쪽으로 시프트 (num이 3이라면 0100)
                        s = s | (1 << num-1);
                        break;
                    case "remove":
                        // ~(1 << num) : num 위치의 숫자를 0으로 하고 나머지를 1로
                        s = s & ~(1 << num-1);
                        break;
                    case "check":
                        // 여기서 '0 <' 는 단순 비교 연산 (0보다 크면 존재한다 (true))
                        if (((1 << num-1) & s) != 0) {
                            writer.write("1\n");
                        } else {
                            writer.write("0\n");
                        }
                        break;
                    case "toggle":
                        if (((1 << num-1) & s) != 0) {
                            // 존재하면
                            s = s & ~(1 << num-1);
                        } else {
                            s = s | (1 << num-1);
                        }
                        break;
                }
            } else {
                switch(op) {
                    case "all":
                        s = s | (1 << 20) - 1;
                        break;
                    case "empty":
                        s = 0;
                        break;
                }
            }
        }
        writer.flush();
        writer.close();
        reader.close();
    }
}