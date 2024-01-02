class Solution {
public:
    string removeStars(string s) {
        std::stack<int> non_star_indices;

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != '*') {
                non_star_indices.push(i);
            } else if (!non_star_indices.empty()) {
                int index = non_star_indices.top();
                non_star_indices.pop();
                s[i] = s[index] = '*';
            }
        }

        std::string result = "";
        for (char c : s) {
            if (c != '*') {
                result += c;
            }
        }

        return result;
    }
};