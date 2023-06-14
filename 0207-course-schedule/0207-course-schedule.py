class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
# create adjacency list
# map every course to an empty list

        preMap = { i:[] for i in range(numCourses)}

        for course, prereq in prerequisites: 
            preMap[course].append(prereq)

    #     visited set to define all the visited courses in the current dfs path
        visited = set()
        def dfs(self, course):
            if course in visited: 
                return False
    #           because there was a cycle detected
            if preMap[course] == []:
                return True
    #         because there are no reqs for this course
            visited.add(course)
            for req in preMap[course]:
                if not dfs(self,req):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(self, course):
                return False
        return True