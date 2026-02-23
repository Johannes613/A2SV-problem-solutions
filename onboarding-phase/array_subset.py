#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        hash_map = {}
        
        for num in a:
            hash_map[num] = hash_map.get(num,0) + 1
        for num in b:
            if num not in hash_map:
                return False
            elif hash_map[num] == 1:
                del hash_map[num]
            else:
                hash_map[num] -= 1
        return True
    
    
    
    
