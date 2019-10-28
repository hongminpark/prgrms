// https://programmers.co.kr/learn/courses/30/lessons/42577?language=java
import java.util.Arrays;


class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < phone_book.length; j++) {
                if (i != j && phone_book[j].startsWith(phone_book[i])) {
                    return false;
                }
            }
        }
        return answer;
    }
}
