def maxSubArray(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
      #print(dp)
    return max(dp)
    
n=int(input())
nums = list(map(int,input().split()))
print(maxSubArray(nums))