import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Set {
    public static void main(String args[]) throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int s = 0;
        int m = Integer.parseInt(reader.readLine().trim());

        for (int i = 0; i < m; i++) {
            String cmd = reader.readLine().trim();
            String[] cmdData = cmd.split(" ");
            String op = cmdData[0];

            if (cmdData.length > 1) {
                int num = Integer.parseInt(cmdData[1]);

                switch (op) {
                    case "add":
                        s = s | (1 << num-1);
                        break;
                    case "remove":
                        s = s & ~(1 << num-1);
                        break;
                    case "check":
                        if (((1 << num-1) & s) != 0) {
                            writer.write("1\n");
                        } else {
                            writer.write("0\n");
                        }
                        break;
                    case "toggle":
                        if (((1 << num-1) & s) != 0) {
                            s = s & ~(1 << num-1);
                        } else {
                            s = s | (1 << num-1);
                        }
                        break;
                }
            } else {
                switch (op) {
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
        reader.close();
        writer.close();
    }
}