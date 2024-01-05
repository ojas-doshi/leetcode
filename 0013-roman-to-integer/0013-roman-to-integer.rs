use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut map = HashMap::new();
        map.insert('I', 1);
        map.insert('V', 5);
        map.insert('X', 10);
        map.insert('L', 50);
        map.insert('C', 100);
        map.insert('D', 500);
        map.insert('M', 1000);

        let mut result = 0;
        let mut prev_value = 0;

        for c in s.chars().rev() {
            let current_value = *map.get(&c).unwrap();
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