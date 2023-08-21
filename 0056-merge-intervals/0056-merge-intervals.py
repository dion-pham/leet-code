class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #start at first index and the index that comes after it
        #make a new list
        
        #if sub[1] >= subB[0]
            #[sub[0],subB[1]]
            
        # for interval in intervals: 

    
        intervals.sort(key = lambda i : i[0])
        
        res = [intervals[0]]
        
        for start,end in intervals[1:]:
            lastEnd = res[-1][1]
            
            if start <= lastEnd: 
                #take the 1st index of the most recent entry and replace it with the larger of the two ends
                res[-1][1] = max(lastEnd,end)
            else: 
                res.append([start,end])
        return res
            
            