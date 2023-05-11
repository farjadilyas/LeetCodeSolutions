class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = [[[], None] for _ in range(numCourses)]
        for prereq in prerequisites:
            hm[prereq[0]][0].append(prereq[1])

        def dfs(course):
            if course[1] is not None: return course[1]
            course[1] = False
            for prereq in course[0]:
                if not dfs(hm[prereq]):
                    return False
            course[1] = True
            return True
        for course in hm:
            if not dfs(course):
                return False
        return True