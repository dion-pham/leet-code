class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # check that the string lengths are equal
        # create hash maps so see if they are equal to each other
        # check to see if the hash map #1 is the same as hash map #2 using the .get method
        # for hashmaps

        if len(s) != len(t):
            return False

        hashA, hashB = {}, {}
        for i in range(len(s)):
            hashA[s[i]] = 1 + hashA.get(s[i], 0)
            hashB[t[i]] = 1 + hashB.get(t[i], 0)
        for key in hashA: 
            if hashA[key] != hashB.get(key, 0):
                return False
        return True