# Bulls and Cows

## Solution 1 - 88.61%

Simple and intuitive !

우리나라 야구게임 하고 똑같은 게임! strike랑 ball갯수를 알려주면 string으로 return해주면 된다.

1. secret이랑 guess한바퀴돌며 동일한거는 A 숫자에 집어넣음
1. 만약 다르면 dic에 key (num) --- value (나온 횟수) 저장, tmp 문자열에 add
1. tmp를 한바퀴 돌며(=secret에서 guess랑 똑같은거 뺀 문자열), 

```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic = {}
        A = 0
        B = 0
        tmp = ''
        for s,g in zip(secret, guess):
            if s == g:
                A+=1
            else:
                tmp += s
                if g in dic:
                    dic[g] += 1
                else:
                    dic[g] = 1
        for s in tmp:
            if s in dic and dic[s] > 0:
                B+=1
                dic[s] -=1
        
        return (str(A) + 'A' + str(B) + 'B')
```