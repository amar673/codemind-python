def fi(nums):  
   i = 0
   nums = [0] + nums
   for i in range(len(nums)):
      while nums[i]>=0 and nums[i]<len(nums) and nums[nums[i]]!=nums[i]:
         nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
      num = 1
      for i in range(1,len(nums)):
         if num == nums[i]:
            num+=1
      return num

a=int(input())
l=list(map(int,input().split()))
print(fi(l))
