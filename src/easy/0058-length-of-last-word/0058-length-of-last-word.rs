impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let trimmed = s.trim();
        let last_word = trimmed.split_whitespace().last().unwrap_or("");
        last_word.len() as i32
    }
}