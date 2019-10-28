// https://programmers.co.kr/learn/courses/30/lessons/42586
import java.util.ArrayList;
import java.util.List;


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int N = progresses.length;
        int[] days = new int[N];
        for (int i = 0; i < N; i++) {
            days[i] = (int) Math.ceil((100 - progresses[i]) / speeds[i]);
        }
        List<Integer> result = new ArrayList<>();
        int release = days[0];
        int count = 1;
        for (int i = 1; i < N; i++) {
            if (days[i] > release) {
                result.add(count);
                release = days[i];
                count = 0;
            }
            count ++;
        }
        result.add(count);
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}
