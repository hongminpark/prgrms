import java.util.HashMap;

public class 완주하지못한선수 {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> part_ = new HashMap<>();
        for (String part: participant) part_.put(part, part_.getOrDefault(part, 0) + 1);
        for (String comp: completion) part_.put(comp, part_.get(comp) - 1);
        String answer = "";
        for (String key: part_.keySet()) {
            if (part_.get(key) != 0) answer = key;
        }
        return answer;
    }

    public static void main(String[] args) {
        완주하지못한선수 obj = new 완주하지못한선수();
        System.out.println(obj.solution(new String[] {"leo", "kiki", "eden"}, new String[] {"eden", "kiki"}));
        System.out.println(obj.solution(new String[] {"mislav", "stanko", "mislav", "ana"}, new String[] {"stanko", "ana", "mislav"}));
    }
}
