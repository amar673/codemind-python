_=int(input())
nums=list(map(int,input().split()))
j = 0
for num in nums:
    if num != 0:
        nums[j] = num
        j += 1
for i in range(j, len(nums)):
    nums[i] = 0
print(*nums)
    