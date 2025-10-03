class Solution(object):
    def canMeasureWater(self,cap_a,cap_b,goal):
        start=(0,0)
        q=deque([start])
        visited=set([start])
        parent={start:None}
        if goal>cap_a+cap_b:
            return False
        while q:
            a,b=q.popleft()
            if a==goal or b==goal or a+b==goal:
                return True
                
            neighbours=[]
            neighbours.append((cap_a,b))
            neighbours.append((a,cap_b))
            neighbours.append((a,0))
            neighbours.append((0,b))
            pour=min(a,cap_b-b)
            neighbours.append((a-pour,b+pour))
            pour=min(cap_a-a,b)
            neighbours.append((a+pour,b-pour))

            for state in neighbours:
                if state not in visited:
                    visited.add(state)
                    parent[state]=(a,b)
                    q.append(state)

        return False