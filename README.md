# Introduction

:speech_balloon: This is the project of :pencil: Problem solving part :pencil: on "Today I learn" 

:speech_balloon: Goals : Clean code, Getting strategic thinking process, Improving problem solving skills...

# Principles

* 1 commit / 1 day == 1 problem / 1 day :heavy_exclamation_mark: at least :heavy_exclamation_mark: 

* Calcuate BigO after solving

* You can get 5 :cherries: for solving performance 

# Reference

- Leetcode
- 구종만 알고리즘 문제 해결전략 
- Cracking the coding interview


# Problem Solving 

## leetcode

#### 532. K-diff Pairs in an Array

:cherries: :cherries:

:white_check_mark: Need to solve one more time

Easy problem. but needs to think twice.
k is absolute difference. Please careful about corner case!
If we delete duplicated elements in array, only need to think i+k.
(because i-k is will be counted on (i-k+k) )


#### 459. Repeated Substring Pattern

:cherries: :cherries: :cherries: :cherries:

:white_check_mark: Find optimal solution

:white_check_mark: O(nlogn)

I didn't look into Other people's solution. :) 

But needs to think of an optimal solution. b/c faster than 49.5%..


#### 763. Partition Labels

:cherries: :cherries:

:white_check_mark: Need to find optimal solution

:white_check_mark: O(N*N)

```python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        startIdx, endIdx = 0,0
        res = []
        for s in S:
            if endIdx == (len(S)-1):
                break
            ns = S.find(s)
            ne = S.rfind(s)
            if ne == ns and ne == 0:
                res.append(1)
                continue
            if ns >= startIdx and ne <= endIdx : 
                continue
            # at least [ns : ne] is one set now..
            for j in range(ns,len(S),1):
                substr = S[j]
                endidx = S.rfind(substr)
                if endidx > ne:
                    ne = endidx
                if j >= ne :
                    break
            # at least [ns : ne] is one set now..
            res.append(ne-ns+1)
            startIdx,endIdx = ns,ne
        return res
```

simple idea. Last index of a letter should be minimum length of one partition.

How about storing last index values.. like Hashtable? 
