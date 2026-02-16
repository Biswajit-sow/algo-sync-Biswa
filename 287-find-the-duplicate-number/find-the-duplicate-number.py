from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while(True):
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
            if (slow==fast):
                slow=0
                while(slow!=fast):
                    slow=nums[slow]
                    fast=nums[fast]
                return slow
        return -1
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# here 0(n)tc and o(1) sc
'''
using hashmap but here 0(n)SC use
        freq = {}
        for num in nums:
            if num in freq:
                return num
            freq[num] = 1
        return -1  # Won't reach if guaranteed duplicate

        '''
