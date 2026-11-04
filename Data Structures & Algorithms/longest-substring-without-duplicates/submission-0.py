class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = 0
        max_length = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            char_set.add(s[j])

            max_length = max(max_length, j - i + 1)

        return max_length