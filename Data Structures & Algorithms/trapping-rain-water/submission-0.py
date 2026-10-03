class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        m_l = 0
        m_r = 0
        for i in range(n):
            m_l = max(m_l,height[i])
            max_left[i] = m_l
        for i in range(n-1,-1,-1):
            m_r = max(m_r,height[i])
            max_right[i] = m_r
        water = 0
        for i in range(n):
            water+=min(max_left[i],max_right[i])-height[i]
        return water