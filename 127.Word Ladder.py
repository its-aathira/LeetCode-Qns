class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList) # to remove duplicates
        if endWord not in wordset:
            return 0
        all_combos = {}
        L=len(beginWord)
        for word in wordset:
            for i in range(L):
                combination = word[:i]+"*"+word[i+1:]
                if combination not in all_combos:
                    all_combos[combination]=[]
                all_combos[combination].append(word)
        queue=[(beginWord,1)]
        visited={beginWord}
        while queue:
            current,level = queue.pop(0)
            for i in range(L):
                combination = current[:i]+"*"+ current[i+1:]
                if combination in all_combos:
                    for next_word in all_combos[combination]:
                        if next_word==endWord:
                            return level+1
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word,level+1))
        return 0
    
            