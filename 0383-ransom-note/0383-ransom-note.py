class Solution(object):
    from collections import defaultdict
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
#       put magazine into a hashmap, (char:occurrences)
#       iterate through ransomNote, subtracting occurences by 1
#          if occ <0, return false
#       return true otherwise

        magazine_char = defaultdict(int)
        for char in magazine: 
            magazine_char[char] += 1
        print(magazine_char)
        for letter in ransomNote: 
            if letter not in magazine_char: 
                return False
            # elif letter in magazine_char: 
            magazine_char[letter] -= 1
            if magazine_char[letter] < 0:
                return False
          
        return True