import java.util.*;

public class CrossCountry {

    static class Position implements Comparable<Position> {
        int pos;
        int team;

        Position(int pos, int team) {
            this.pos = pos;
            this.team = team;
        }

        @Override
        public int compareTo(Position o) {
            return Integer.compare(this.pos, o.pos);
        }
    }

    private static int sum(List<Integer> list) {
        int sum = 0;
        for (int num : list) {
            sum += num;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();
            int[] teams = new int[N];
            for (int i = 0; i < N; i++) {
                teams[i] = sc.nextInt();
            }

            Map<Integer, List<Integer>> teamMembers = new HashMap<>();

            // 팀별 주자 등수
            for (int i = 0; i < N; i++) {
                int team = teams[i];
                teamMembers.putIfAbsent(team, new ArrayList<>());
                teamMembers.get(team).add(i+1);
            }

            // 6명이상팀 필터링 
            Map<Integer, List<Integer>> validTeams = new HashMap<>();
            for (Map.Entry<Integer, List<Integer>> entry : teamMembers.entrySet()) {
                if (entry.getValue().size() >= 6) {
                    validTeams.put(entry.getKey(), entry.getValue());
                }
            }

            // validTeams로 새로운 순위 매김
            List<Position> allPositions = new ArrayList<>();
            for (Map.Entry<Integer, List<Integer>> entry : validTeams.entrySet()) {
                int team = entry.getKey();
                for (int pos : entry.getValue()) {
                    allPositions.add(new Position(pos, team));
                }
            }
            // 정렬
            Collections.sort(allPositions);
            
            // 점수 부여
            Map<Integer, List<Integer>> scoreList = new HashMap<>();
            for (int i = 0; i < allPositions.size(); i++) {
                Position p = allPositions.get(i);
                scoreList.putIfAbsent(p.team, new ArrayList<>());
                scoreList.get(p.team).add(i + 1);
            }

            // 상위 4명 점수 계산 및 우승팀
            int minScore = Integer.MAX_VALUE;
            int winner = -1;

            for (Map.Entry<Integer, List<Integer>> entry : scoreList.entrySet()) {
                int team = entry.getKey();
                List<Integer> scores = entry.getValue();
                int teamScore = sum(scores.subList(0,4));

                if (teamScore < minScore) {
                    minScore = teamScore;
                    winner = team;
                }
                else if (teamScore == minScore) {
                    if (scores.get(4) < scoreList.get(winner).get(4)) winner = team;
                }
            }

            System.out.println(winner);

        }
    }   
}


