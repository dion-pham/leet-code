class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create an adjacency list for courses
        #iterate through adj list, 
            #keep track of visited courses with a set
            #dfs with recursion to the end of each course   
                #if any course is already in visited, but youre visiting it again, that means that its not a valid course schedule
        # return true if the above does not happen
        
        courseSchedule = {}
        for i in range(numCourses):
            courseSchedule[i] = []

        for prereq in prerequisites:
            a,b = prereq
            courseSchedule[a].append(b)
            
        visited = set()
        
        def dfs(self, course):
            #base case: keep track of visited
            if course in visited: return False
            #base case: take into account that if x:[], there are no previous reqs                 for a course
            if courseSchedule[course] == []:
                return True
      
            
            visited.add(course)
            
            for prereq in courseSchedule[course]:
                
                if not dfs(self,prereq):
                    return False
            visited.remove(course)
            courseSchedule[course] = []
            return True
                
                
        for course in range(numCourses):
            if not dfs(self, course):
                return False
            
        return True
    
 