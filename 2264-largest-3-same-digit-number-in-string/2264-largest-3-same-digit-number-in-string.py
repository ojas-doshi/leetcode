class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = ""
        sub_string_dict = defaultdict(int)
        last_range_pt = len(num)-2 if len(num) > 3 else 1
        for i in range(0,last_range_pt):
            sub_string = set(ch for ch in num[i:i+3])
            print(sub_string)
            if len(sub_string) == 1:
                sub_string_dict[int("".join(sub_string))] = i
                result = sub_string
        sub_keys = sub_string_dict.keys()
        if sub_keys:
            value = sub_string_dict[max(sub_keys)]
            result = num[value:value+3]
        return result 