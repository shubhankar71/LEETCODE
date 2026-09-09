'''
Concatenate Non-Zero Digits and Multiply by Sum II

You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].
For each queries[i], extract the substring s[li..ri]. Then, perform the following:
Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.

Example 1:
Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]
Output: [12340, 4, 9]
Explanation:
s[0..7] = "10203004"
x = 1234
sum = 1 + 2 + 3 + 4 = 10
Therefore, answer is 1234 * 10 = 12340.
s[1..3] = "020"
x = 2
sum = 2
Therefore, the answer is 2 * 2 = 4.
s[4..6] = "300"
x = 3
sum = 3
Therefore, the answer is 3 * 3 = 9.

Example 2:
Input: s = "1000", queries = [[0,3],[1,1]]
Output: [1, 0]
Explanation:
s[0..3] = "1000"
x = 1
sum = 1
Therefore, the answer is 1 * 1 = 1.
s[1..1] = "0"
x = 0
sum = 0
Therefore, the answer is 0 * 0 = 0.

Example 3:
Input: s = "9876543210", queries = [[0,9]]
Output: [444444137]
Explanation:
s[0..9] = "9876543210"
x = 987654321
sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
Therefore, the answer is 987654321 * 45 = 44444444445.
We return 44444444445 modulo (109 + 7) = 444444137.
'''

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
