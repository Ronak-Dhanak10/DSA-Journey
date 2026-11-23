# Given an array arr of positive integers and an integer x. Return the frequency of x in the array
class Solution:
    def findFrequency(self, arr, x):
        d = {}
        for i in arr:
            d[i]=d.get(i,0)+1
        return d.get(x,0)