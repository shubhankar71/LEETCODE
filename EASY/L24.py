class Solution:
    def plusOne(self, digits):
        n = []
        for i in digits[:]:
            n.append(str(i))
            digits.remove(i)
        m = str(int("".join(n)) + 1)
        for i in range(len(m)):
            digits.append(int(m[i]))
            
        return digits

