class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum_apple=sum(apple)
        capacity.sort(reverse=True)


        for i ,box_caps in enumerate(capacity):
            sum_apple-=box_caps
            if sum_apple<=0:
                return i+1
        '''box_used=0
        for box_caps in capacity:
            sum_apple-=box_caps
            box_used+=1
            if sum_apple<=0:
                break
        return box_used'''
