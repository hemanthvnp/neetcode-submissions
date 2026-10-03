class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        s1 = [0] * n
        s2 = []

        for i in range(n):
            while s2 and temperatures[i] > temperatures[s2[-1]]:
                prev = s2.pop()
                s1[prev] = i - prev

            s2.append(i)

        return s1