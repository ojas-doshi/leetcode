class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        def generate_sequential(curr_num):
            if low <= curr_num <= high:
                result.append(curr_num)

            last_digit = curr_num % 10
            if last_digit < 9:
                new_num = curr_num * 10 + (last_digit + 1)
                generate_sequential(new_num)

        for start_digit in range(1, 10):
            generate_sequential(start_digit)

        return sorted(result)