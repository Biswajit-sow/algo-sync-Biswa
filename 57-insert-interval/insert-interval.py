class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        n=len(intervals)
        start1=intervals[0][0]
        end1=intervals[0][1]
        for i in range(1,n):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if (end1>=start2):
                start1=start1#min
                end1=max(end1,end2)
                continue
            res.append([start1,end1])
            start1=start2
            end1=end2

        res.append([start1,end1])
        return res