import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class 가장먼노드 {
    public int solution(int n, int[][] edge) {
        HashMap<Integer, List<Integer>> edges = new HashMap<>();
        for (int[] e: edge) {
            List<Integer> e_1 = edges.getOrDefault(e[0], new ArrayList<>());
            e_1.add(e[1]);
            edges.put(e[0], e_1);
            List<Integer> e_2 = edges.getOrDefault(e[1], new ArrayList<>());
            e_2.add(e[0]);
            edges.put(e[1], e_2);
        }
        int[] visited = new int[n+1];
        visited[1] = 1;
        List<Integer> stack = new ArrayList<>();
        stack.add(1);
        while (true) {
            List<Integer> tmp_stack = new ArrayList<>();
            for (int now: stack) {
                List<Integer> nexts = edges.get(now);
                for (int next: nexts) {
                    if (visited[next] == 0) {
                        visited[next] = 1;
                        tmp_stack.add(next);
                    }
                }
            }
            if (tmp_stack.size() > 0) stack = tmp_stack;
            else return stack.size();
        }
    }
    public static void main(String[] args) {
        가장먼노드 obj = new 가장먼노드();
        System.out.println(obj.solution(6,
                new int[][] {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}}));

    }
}


