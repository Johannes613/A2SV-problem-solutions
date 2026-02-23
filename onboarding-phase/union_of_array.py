class Solution:    
    def findUnion(self, a, b):
        hash_set = set()
        
        for num in a:
            hash_set.add(num)
        for num in b:
            hash_set.add(num)
            
        return list(hash_set)
        