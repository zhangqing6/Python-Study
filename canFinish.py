class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        # 0未访问 1访问中 2已完成
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False  # 遇到回路
            if visited[course] == 2:
                return True
            visited[course] = 1
            # 遍历所有后继
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            visited[course] = 2
            return True
        
        # 遍历所有课程
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
