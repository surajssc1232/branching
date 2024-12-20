n=int(input())
nums = [int(x) for x in input().split()][:n]

# 3 2 5 1 7
count = 0
for i in range(1, len(nums)-1):
    if not nums[i-1] < nums[i] < nums[i+1]:
        while nums[i] <= nums[i-1] or nums[i] >= nums[i+1]:
            nums[i] += 1
            count += 1

print(count)



