# 22. Generate Parentheses

# Solution 1 
# Think like a tree and Use DFS. make a valid string every time and when is done, add them in the list.
# Time Complexity : O(N*N) -  beat 81.12% 
# Solutino says, time complexity for this is O(4^n / sqr(n))
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(num,str,left,r):
                # num = '(' left parenthesis number wating to be pair!
                # left = '(' nums left
                if num == 0 and left == 0:
                        r.append(str)
                        return str
                if num > 0 :
                        generate(num-1,str+')',left,r)
                        if left > 0:
                                generate(num+1, str+'(', left-1,r)
                if num == 0 and left > 0 :
                        generate(num+1, str+'(', left-1,r)
        res = []
        generate(0,"",n,res)
        return res
