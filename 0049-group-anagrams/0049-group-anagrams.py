class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through the list
        #{aet:[eat,tea], abt:[],ant:[]}
            #return object.values 
            
        sortedHash = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in sortedHash:
                sortedHash[sortedWord] = []
                sortedHash[sortedWord].append(word)
            else: 
                sortedHash[sortedWord].append(word)
        return sortedHash.values()
            
        
        