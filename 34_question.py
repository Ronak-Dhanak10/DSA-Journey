# Frequencies in a Limited Array
class Solution:
    def frequencyCount(self, arr):
        d= {}
        for i in arr:
           d[i]=d.get(i,0)+1
        values = []
        
        for i in range(1,len(arr)+1):
            values.append(d.get(i,0))
        return values
       
