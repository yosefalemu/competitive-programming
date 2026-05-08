class Solution:
    def reverseWords(self, s: str) -> str:
        slow_pt = 0
        ans = []
        for fast_pt in range(len(s)):
            if s[slow_pt] == " ":
                slow_pt += 1
                continue
            if s[fast_pt] == " ":
                ans.append(s[slow_pt: fast_pt])
                slow_pt = fast_pt + 1
            elif fast_pt == len(s) - 1:
                ans.append(s[slow_pt: fast_pt + 1])
        ans.reverse()
        return " ".join(ans)

        