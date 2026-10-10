# OPTIMAL SOL ---> {GREEDY} ---> DAILY QUESTION (09 SEPT 2026)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        result = 0

        count = 0
        skip = False

        for i in range(n):
            if skip:
                skip = False
                continue

            if s[i] == '(':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    result += 1
                
                if i + 1 < n and s[i + 1] == ')':
                    skip = True
                else:
                    result += 1

        return result + 2 * count

# T.C : O(n)
# S.C : O(1)