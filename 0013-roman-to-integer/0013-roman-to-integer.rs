impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut result = 0;
        let mut prev_value = 0;

        for c in s.chars().rev() {
            let current_value = match c {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _ => 0, // Handle invalid characters
            };

            if current_value < prev_value {
                result -= current_value;
            } else {
                result += current_value;
            }
            prev_value = current_value;
        }

        result
    }
}
