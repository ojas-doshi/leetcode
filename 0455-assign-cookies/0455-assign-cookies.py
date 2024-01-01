class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0  # Pointer for children
        j = 0  # Pointer for cookies
        content_children = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_children += 1
                i += 1
            j += 1

        return content_children
