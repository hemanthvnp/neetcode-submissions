class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        s = []
        max_area = 0

        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                l = s.pop()
                height = heights[l]
                if not s:
                    width = i
                else:
                    width = i-s[-1]-1
                area = height * width
                max_area = max(max_area, area)
            s.append(i)

        return max_area