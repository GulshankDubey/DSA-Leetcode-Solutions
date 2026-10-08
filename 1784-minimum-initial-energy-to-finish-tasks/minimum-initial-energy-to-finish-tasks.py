# OPTIMAL SOL ---> {Binary search on answer + greedy sorting} ---> DAILY QUESTION (SEPT 2026)
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        n = len(tasks)

        l = 0
        r = 10**9

        result = float('inf')

        tasks.sort(key = lambda task: task[1] - task[0], reverse = True)

        while l <= r:
            mid = l + (r-l) // 2

            if self.ispossible(tasks, mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return result

    def ispossible(self, tasks, mid):
        for task in tasks:
            actual = task[0]
            minimum = task[1]

            if minimum > mid:
                return False

            mid -= actual
        
        return True

# T.C : O(n*logn)
# S.C : O(1)


