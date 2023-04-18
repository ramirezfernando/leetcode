class Solution:
    def mergeAlternately(self, word1, word2):

        w1 = 0
        w2 = 0
        output = ""
        while w1 < len(word1) and w2 < len(word2):
            output += word1[w1]
            output += word2[w2]
            w1 += 1
            w2 += 1

        while w1 < len(word1):
            output += word1[w1]
            w1 += 1

        while w2 < len(word2):
            output += word2[w2]
            w2 += 1

        return output