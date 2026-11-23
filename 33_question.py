# Leetcode 1207. Unique Number of Occurrences
class Solution(object):
    def uniqueOccurrences(self, arr):
       d= {}
       for i in arr:
          d[i] = d.get(i,0)+1
       values=list(d.values())
       set(values)
       if len(values) == len(set(values)):
         return True
       else:
         return False

