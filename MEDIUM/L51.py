class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)
        
        suf = [m] * (n + 1)

        for i in range(n - 1, -1, -1):
            j = suf[i + 1]

            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1

            suf[i] = j

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one allowed change
            elif not changed and suf[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                changed = True

        if j == m:
            return ans

        return []