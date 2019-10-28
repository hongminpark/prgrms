// https://programmers.co.kr/learn/courses/30/lessons/42626
import java.util.PriorityQueue;


class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int scov: scoville) {
            priorityQueue.add(scov);
        }
        while (priorityQueue.peek() < K) {
            if (priorityQueue.size() == 1) {
                if (priorityQueue.poll() < K) {
                    return -1;
                } else {
                    return answer;
                }
            }
            int first = priorityQueue.poll();
            int second = priorityQueue.poll();
            int new_ = first + (2 * second);
            priorityQueue.add(new_);
            answer ++;
        }
        return answer;
    }
}
