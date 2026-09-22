class Solution(object):

    def isPalindrome(self, s):

        def check(i):

            if i >= len(s) // 2:
                return True

            if s[i] != s[len(s) - i - 1]:
                return False

            return check(i + 1)

        return check(0)
    

        