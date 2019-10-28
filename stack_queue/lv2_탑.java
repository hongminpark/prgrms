// https://programmers.co.kr/learn/courses/30/lessons/42588
class Solution {
    public int[] solution(int[] heights) {
        int N = heights.length;
        int[] answer = new int[N];
        for (int i = N-1; i >= 0; i--) {
            int razor = 0;
            for (int j = i-1; j >= 0; j--) {
                if (heights[j] > heights[i]) {
                    razor = j+1;
                    break;
                }
            }
            answer[i] = razor;
        }
        return answer;
    }
}
