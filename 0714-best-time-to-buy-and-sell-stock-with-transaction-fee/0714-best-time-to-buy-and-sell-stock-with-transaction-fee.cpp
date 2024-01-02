class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (prices.empty()) return 0;

        int n = prices.size();
        std::vector<int> buy(n);
        std::vector<int> sell(n);

        buy[0] = -prices[0] - fee;

        for (int i = 1; i < n; ++i) {
            buy[i] = std::max(buy[i - 1], sell[i - 1] - prices[i] - fee);
            sell[i] = std::max(sell[i - 1], buy[i - 1] + prices[i]);
        }

        return sell[n - 1];
    }
};