impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::new();
        }

        let mut prefix = String::new();
        let first_word = strs[0].as_bytes();

        'outer: for i in 0..first_word.len() {
            let current_char = first_word[i];

            for j in 1..strs.len() {
                if i >= strs[j].len() || strs[j].as_bytes()[i] != current_char {
                    break 'outer;
                }
            }

            prefix.push(current_char as char);
        }

        prefix
    }
}
