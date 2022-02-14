class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        wordlist = list(s)
        length = len(wordlist)
        longest_substring_len = 0; length_of_word = 0
        for i in range(length):
            for j, word in enumerate(wordlist[i:]):
                if word not in wordlist[i:i+j]:
                    length_of_word += 1
                else:
                    break
            if length_of_word > longest_substring_len:
                longest_substring_len = length_of_word
            length_of_word = 0
        return longest_substring_len
'''
时间复杂度 O(n^3)  因为 not in a list 也用时n
'''
    def lengthOfLongestSubstring2(self, s: str) -> int:

solution1 = Solution()
result = solution1.lengthOfLongestSubstring1("helloworld")
print(result)
