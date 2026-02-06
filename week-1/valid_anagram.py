class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for ch in s:
            hash_map[ch] = hash_map.get(ch,0) + 1
        
        for ch in t:
            if ch not in hash_map:
                return False
            elif hash_map[ch] == 1:
                del hash_map[ch]
            else:
                hash_map[ch] -= 1
                
        return len(hash_map) == 0


        
        