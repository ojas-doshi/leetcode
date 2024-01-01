class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def check_divisibility(string, divisor):
            return string == (divisor * (len(string) // len(divisor)))

        if str1 + str2 != str2 + str1:
            return ""

        divisor_length = gcd(len(str1), len(str2))
        divisor = str1[:divisor_length]

        if check_divisibility(str1, divisor) and check_divisibility(str2, divisor):
            return divisor
        else:
            return ""
