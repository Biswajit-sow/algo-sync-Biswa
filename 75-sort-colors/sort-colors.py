class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_arr=[]
        zero=0
        one=0
        two=0
        n=len(nums)
        for i in nums:
            if i==0:
                zero+=1
                
            elif i==1:
                one+=1
                
            elif i==2:
                two+=1
         # Second pass: modify nums in-place
        #sorted_arr = [0]*zero + [1]*one + [2]*two

        for i in range(zero):
            sorted_arr.append(0)
        for j in range(one):
            sorted_arr.append(1)
        for k in range(two):
            sorted_arr.append(2)
        
        for i in range(len(nums)):
            nums[i] = sorted_arr[i]

            
       



                    



            