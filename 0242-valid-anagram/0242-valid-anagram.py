class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in str(s):
            s_dict[i] +=1
        for i in str(t):
            t_dict[i] +=1
        return s_dict == t_dict