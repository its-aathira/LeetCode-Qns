class Solution(object):
    def buildArray(self, target, n):
        operations=[]
        current=1
        for num in target:
            while current<num:
                operations.append("Push")
                operations.append("Pop")
                current+=1
            operations.append("Push")
            current+=1
        return operations

        