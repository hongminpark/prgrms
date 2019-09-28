// https://programmers.co.kr/learn/courses/30/lessons/42839

import java.util.HashSet;


class Solution {
    public int solution(String numbers) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        permutation("", numbers, set);
        while (set.iterator().hasNext()) {
            int now = set.iterator().next();
            if (isPrime(now)) {
                answer ++;
            }
            set.remove(now);
        }
        return answer;
    }

    public boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public void permutation(String begin, String end, HashSet<Integer> result) {
        if (!begin.equals("")) result.add(Integer.valueOf(begin));
        for (int i = 0; i < end.length(); i++) {
            permutation(begin + end.charAt(i), end.substring(0, i) + end.substring(i+1, end.length()), result);
        }
    }
}
