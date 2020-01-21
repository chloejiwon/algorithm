class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in reversed(range(len(s))):
            if i == 0 : continue
            # i should be the factor of len(s) 
            if len(s) % i != 0:
                continue
            # chuk_size is i
  #          print i
            basicStr, isMatched = s[0:i] ,True
  #          print "Basic String : " ,basicStr
            for j in range( len(s)/i ):
  #              print "Comparing String :" ,  s[i*j: i*j + i]
                if basicStr != s[i*j: i*j + i]:
                    isMatched = False
                    break
                    
            if isMatched:
                return True
            
        return False

