# Write a Python program to find the length of the last word in a string.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        words = s.split()
        return len(words[-1])
      