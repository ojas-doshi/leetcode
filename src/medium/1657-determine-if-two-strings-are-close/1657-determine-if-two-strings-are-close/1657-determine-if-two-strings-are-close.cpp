class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        std::unordered_map<char, int> freq1, freq2;
        std::unordered_map<int, int> countFreq1, countFreq2;

        for (char ch : word1) {
            freq1[ch]++;
        }

        for (char ch : word2) {
            freq2[ch]++;
        }

        for (const auto &entry : freq1) {
            countFreq1[entry.second]++;
        }

        for (const auto &entry : freq2) {
            countFreq2[entry.second]++;
        }

        if (countFreq1 == countFreq2) {
            for (const auto &entry : freq1) {
                if (freq2.find(entry.first) == freq2.end()) {
                    return false;
                }
            }
            return true;
        }

        return false;
    }
};