impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        let mut total_gas = 0;
        let mut curr_gas = 0;
        let mut start_index = 0;

        for i in 0..n {
            total_gas += gas[i] - cost[i];
            curr_gas += gas[i] - cost[i];

            if curr_gas < 0 {
                curr_gas = 0;
                start_index = i + 1;
            }
        }

        if total_gas >= 0 {
            start_index as i32
        } else {
            -1
        }
    }
}