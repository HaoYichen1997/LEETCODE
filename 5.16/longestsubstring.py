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
        slide_window_left = 0; slide_window_right = 0
        wordlist = list(s)
        length = len(wordlist)
        longest_substring_len = 0; window_side = 0;
        slide_window_dict = dict()
        for right, word in enumerate(wordlist):
            if word not in slide_window_dict:
                slide_window_right += 1
                slide_window_dict[word] = right
                window_side += 1
                if window_side > longest_substring_len:
                    longest_substring_len = window_side
            else:
                while word in slide_window_dict:
                    del slide_window_dict[wordlist[slide_window_left]]
                    slide_window_left += 1
                    window_side -= 1
                slide_window_dict[word] = right
                window_side += 1
        return longest_substring_len
'''
滑动窗口，时间复杂度为O(n)，无论滑动结果如何都是常数项操作
'''

solution1 = Solution()
result = solution1.lengthOfLongestSubstring2("helloworld")
print(result)
