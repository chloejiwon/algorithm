class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        time = 0
        while counter.most_common()[0][1] >= 1:
            left = 0
            for t in counter:
                if counter[t] > 0:
                    left += 1
            c = counter.most_common()
            
            deleted = []
            if n < left:
                time += n+1
                for i in range(n+1):
                    deleted += c[i][0]
                counter.subtract(deleted)
            else:
                if c[0][1] >= 2:
                    time += n+1
                else:
                    time += left
                counter.subtract(counter.keys())
            
        return time
