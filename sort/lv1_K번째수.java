// https://programmers.co.kr/learn/courses/30/lessons/42748
import java.util.Arrays;


class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int N = commands.length;
        int[] answer = new int[N];
        for (int i = 0; i < N; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][0]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }
        return answer;
    }
}
