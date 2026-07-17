class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={i:[] for i in range(numCourses)}
        indegree = [0]* numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course]+=1
        queue=[i for i in range(numCourses) if indegree[i]==0]
        processed_courses = 0
        while queue:
            current_course = queue.pop(0)
            processed_courses+=1
            for neighbour in adj_list[current_course]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return processed_courses == numCourses

        