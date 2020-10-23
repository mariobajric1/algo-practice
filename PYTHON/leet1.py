# longest palindrome in string
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':

        #       if the length of the string is 0/1, return the string
        if len(s) <= 1:
            return s

#       start, end values of panlindrome set to 0
        start = end = 0
#       length var is set length of the string
        length = len(s)
#       loop in the range of the length
        for i in range(length):

            max_len_1 = self.get_max_len(s, i, i + 1)
            max_len_2 = self.get_max_len(s, i, i)

            max_len = max(max_len_1, max_len_2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end+1]

#    define helper function
    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':

        #       length var is set length of the string
        length = len(s)
#       while Leftpointer is greater than 0 and rightpointer is less than the length, and their values are equal
        while left >= 0 and right < length and s[left] == s[right]:
            #              decrement left pointer
            left -= 1
#             increment left pointer
            right += 1
#     return right-left-1
        return right - left - 1
