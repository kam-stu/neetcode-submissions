class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_words = {}
        for word in strs:
            trie = [0] * 26
            for char in word:
                # subtracting ord('a') gives us position relative to alphabet
                trie[ord(char) - ord('a')] += 1
            trie = tuple(trie)
            # after trie is complete, add it to the all_words hashmap
            if (all_words.get(trie) is None):
                all_words[trie] = [word]
            else:
                all_words[trie].append(word)
            
        return list(all_words.values())

            