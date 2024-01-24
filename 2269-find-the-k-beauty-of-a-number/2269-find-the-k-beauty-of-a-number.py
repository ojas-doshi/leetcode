class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        def count_divisibles():
            num_str = str(num)
            for i in range(len(num_str)-k+1):
                print(num_str[i:i+k])
                yield num % int(num_str[i:i+k]) == 0 if int(num_str[i:i+k]) > 0 else 0
        return sum(count_divisibles())