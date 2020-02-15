# 17. Letter Combinations of a Phone Number
# [Medium] Backtracking

# Solution 1
# Recursion
# O(n) - beat 79% 
# make one letters, and then next one adding letters.. and so on 
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict,res = {},[]
        dict[2],dict[3],dict[4],dict[5],dict[6],dict[7],dict[8],dict[9] = ['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']
        def tracking(previous,n):
                letters = []
                for j in dict[n]:
                        tmp = []
                        for s in previous:
                                tmp.append(s+j)
                        letters+= tmp
                return letters
        for i,s in enumerate(digits):
                if i==0:
                    res = dict[int(s)]
                else : 
                    res = tracking(res,int(s))
        return res

