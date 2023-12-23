class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = ""
        sub_string_dict = dict()
        for i in range(0,len(num)-2 if len(num) > 3 else 1):
            sub_string = set(ch for ch in num[i:i+3])
            if len(sub_string) == 1:
                sub_string_dict[int("".join(sub_string))] =  num[i:i+3]
        if sub_string_dict.keys():
            result = sub_string_dict[max(sub_string_dict.keys())]
        return result 