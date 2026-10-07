# OPTIMAL SOL ---> {Calculating from Depth}--->(DAILY QUESTION 5 OCT 2026)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        depth = 0
        score = 0

        for i in range(n):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1

                if s[i-1] == '(':
                    score += (1 << depth)
        return score

# TC : O(n)
# SC : O(1)