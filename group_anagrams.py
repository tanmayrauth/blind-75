"""
The naive logic which I first thought of is that either use a counter for the string or sort the string and then compare which all are same. 
But thts a very naive a time consuming approach since sorting the list itself will take nlogn time.
To make it optimal logic is that since number of char are limited (26) why not we create a list of 26 index and use its tuple version as key for our dict to store all anagrams.
Your 26 indexes list will store the count of each char in a particular word. And now if that tuple is same then we append it to our result dict list
        
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) 
        for s in strs:
            count = [0]*26 
            for i in s:
                count[ord(i) - ord('a')] += 1 
            res[tuple(count)].append(s) 

        return res.values()