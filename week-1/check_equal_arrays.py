class Solution:
    def checkEqual(self, a, b) -> bool:
        if(len(a) != len(b)): return False
        
        hash_map = {}
        
        for num in a:
            hash_map[num] = hash_map.get(num,0) + 1
            
        for num in b:
            if num not in hash_map:
                return False
            else:
                if hash_map[num] == 1:
                    del hash_map[num]
                else:
                    hash_map[num] -= 1
                    
                
        return len(hash_map) == 0    
        
        