"""
 You need to encode the whole list of string to a string and then decode it. 
 The algorithm with NC applied was that for each word while storing it to string we will save it as length#Word format for each word. 
 And in decode function it will seach for # symbol and take the char before it convert 
 it to int and that no is used to find the next lenght after # symbol in that encoded string.
"""

class Solution:

    def encode(self, strs):
        res=""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str);
        res = []
        ctr = 0

        while ctr < len(str):
            l = ctr
            
            while str[l] != "#":
                l += 1

            length = int(str[i:l]) # Getting the str length value
            res.append(str[l : l+length+1]) # Fetching the actual string

            ctr = l+length+i

        return res

            