class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.rbegin(), citations.rend()); // Sort the citations in descending order
        int n = citations.size();
        int h_index = 0;

        for (int i = 0; i < n; ++i) {
            if (citations[i] >= i + 1) {
                h_index = i + 1;
            } else {
                break;
            }
        }

        return h_index;
    }
};