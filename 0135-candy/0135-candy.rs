impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        if n <= 1 {
            return n as i32;
        }

        let mut candies = vec![1; n];

        // Scan from left to right, if the right child has a higher rating, give more candies
        for i in 1..n {
            if ratings[i] > ratings[i - 1] {
                candies[i] = candies[i - 1] + 1;
            }
        }

        // Scan from right to left, if the left child has a higher rating and fewer candies, update candies
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] {
                candies[i] = std::cmp::max(candies[i], candies[i + 1] + 1);
            }
        }

        candies.iter().sum()
    }
}