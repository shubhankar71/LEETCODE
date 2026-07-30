class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        m = []
        for i in range(len(s)):
            if s[len(s)-1-i]!=" ":
                m.append(s[len(s)-1-i])
            else:
                break
        return len(m)
