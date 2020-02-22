# 973. K Closest Points to Origin

# Solution 1
# Time Complexity :  O(n + nlogn) = O(nlogn)
# 1, figure out each distance between origin and point.and make index & distance into dictionary.
# 2, sort dictionary with values.
# 3, Only pop k elements in the distance.
# Beat 84.76%
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist,i = {},0
        for point in points:
                dist[i] = point[0]*point[0] + point[1]*point[1]
                i+=1
        dist = sorted(dist.items(),key = lambda x:x[1])
        res = []
        for i in range(K):
                res.append(points[dist[i][0]])
        return res

# Solution 2 (** need to do **)
# Divide and conquer solution
