#include <vector>
#include <stack>

class Solution {
public:
    int sumSubarrayMins(std::vector<int>& arr) {
        const int MOD = 1000000007;
        int n = arr.size();
        std::vector<int> left(n), right(n);

        std::stack<int> st;

        // Calculate the next smaller element on the left for each element
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && arr[i] < arr[st.top()]) {
                st.pop();
            }

            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        // Clear the stack for the next iteration
        while (!st.empty()) {
            st.pop();
        }

        // Calculate the next smaller element on the right for each element
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && arr[i] <= arr[st.top()]) {
                st.pop();
            }

            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }

        long long result = 0;

        // Calculate the sum of minimums for each subarray
        for (int i = 0; i < n; ++i) {
            result = (result + (long long)arr[i] * (i - left[i]) * (right[i] - i) % MOD) % MOD;
        }

        return static_cast<int>(result);
    }
};
