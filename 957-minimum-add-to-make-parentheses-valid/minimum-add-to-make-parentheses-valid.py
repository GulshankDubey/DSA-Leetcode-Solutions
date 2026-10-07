# OPTIMAL SOL ---> DAILY QUESTION (06 SEPT 2026)
# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         n = len(s)
#         depth = 0
#         ans = 0

#         for i in range(n):
#             if s[i] == '(':
#                 depth += 1
#             elif s[i] == ')':
#                 depth -= 1
#             if depth < 0:
#                 ans += 1
#                 depth = 0

#         return max(ans , ans + depth)

                # BOTH ARE TRUE AND SAME-SAME
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth = 0
        ans = 0

        for ch in s:
            if ch == '(':
                depth += 1
            else:
                depth -= 1

                if depth < 0:
                    ans += 1
                    depth = 0

        return ans + depth

# TC : O(n)
# SC : O(1)