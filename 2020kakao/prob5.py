# https://programmers.co.kr/learn/courses/30/lessons/60061

class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word):
        cur = self.head
        for char in word:
            cur.setdefault(char, {})
            cur = cur[char]
        cur["*"] = True

    def query(self, query):
        cur = self.head
        count = 0
        for idx, char in enumerate(query):
            if char == "?":
                stack = list(cur.values())
                for _ in range(len(query) - idx - 1):
                    tmp = []
                    for node in stack:
                        if type(node) is dict:
                            tmp += node.values()
                    stack = tmp
                return sum([1 for item in stack if type(item) is dict and "*" in item])
            elif char not in cur:
                return count
            else:
                cur = cur[char]


def solution(words, queries):
    trie = Trie()
    trie_reversed = Trie()
    maxlen = max([len(q) for q in queries])

    for word in words:
        if len(word) <= maxlen:
            trie.insert(word)
            trie_reversed.insert(word[::-1])

    result = []
    for query in queries:
        if query.startswith("?"):
            result.append(trie_reversed.query(query[::-1]))
        else:
            result.append(trie.query(query))

    return result

