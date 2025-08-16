def findMaxAverage(nums, k):
        i = 0
        j = k
        total = float("-inf")
        count = sum(nums[:k])
        total = count
        while j < len(nums):
            count -= nums[i]
            count += nums[j]
            i +=1
            j +=1
            total = max(total, count)
        return total / k
