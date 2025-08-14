class Solution:
    def merge(self, nums1, m, nums2, n):
        
        nums1_copy = nums1[:m]
        i = j = 0
        k=0
        while i < m and j < n:
           
            if nums1_copy[i] < nums2[j]:
                nums1[k] =nums1_copy[i]
                i += 1

            else:
                nums1[k]=nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] =nums1_copy[i]
            i += 1
            k +=1
        
        while j < n:
            nums1[k]=nums2[j]
            j += 1
            k +=1
        print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3   
nums2 = [2,5,6]
n = 3   
solution = Solution()
solution.merge(nums1, m, nums2, n) 
