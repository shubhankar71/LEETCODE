class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        count = [0] * (n + 1)
        powers = [1] * (n + 1)

        for i in range(n):
            digit = int(s[i])

            prefix_sum[i + 1] = prefix_sum[i]
            prefix_num[i + 1] = prefix_num[i]
            count[i + 1] = count[i]

            if digit != 0:
                prefix_sum[i + 1] += digit
                prefix_num[i + 1] = (
                    prefix_num[i] * 10 + digit
                ) % MOD
                count[i + 1] += 1

            powers[i + 1] = (powers[i] * 10) % MOD

        answer = []

        for l, r in queries:
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            cnt = count[r + 1] - count[l]

            if cnt == 0:
                answer.append(0)
                continue
            x = (
                prefix_num[r + 1]
                - prefix_num[l] * powers[cnt]
            ) % MOD

            answer.append((x * digit_sum) % MOD)

        return answer