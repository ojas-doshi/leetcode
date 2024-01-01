class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) {
            return false;
        }

        int minVal = std::numeric_limits<int>::max();
        int secondMin = std::numeric_limits<int>::max();

        for (int num : nums) {
            if (num <= minVal) {
                minVal = num;
            } else if (num <= secondMin) {
                secondMin = num;
            } else {
                return true;
            }
        }

        return false;
    }
};