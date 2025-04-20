import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Person {
    int weight, height;

    Person(int weight, int height) {
        this.weight = weight;
        this.height = height;
    }
}

public class Big {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        
        ArrayList<Person> people = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int weight = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());

            people.add(new Person(weight,height));
        }

        for (int i = 0; i < N; i++) {
            int rank = 1;
            for (int j = 0; j < N; j++) {
                if (people.get(i).weight < people.get(j).weight && people.get(i).height < people.get(j).height) {
                    rank++;
                }
            }
            if (i == N-1) System.out.println(rank);
            else System.out.print(rank + " ");
            
        }
    }
}