import bisect

class Solution:
    def printLIS(self, nums, parent, best_i):
        if parent[best_i] != best_i:
            self.printLIS(nums, parent, parent[best_i])
        print(nums[best_i])


    def lengthOfLSTWithPrint(self, nums):
        best, best_i = 0, 0
        length = [1 for _ in range(len(nums))]
        parent = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and length[i] < length[j] + 1:
                    length[i] = length[j] + 1
                    parent[i] = j
                    if length[i] > best:
                        best, best_i = length[i], i

        self.printLIS(nums, parent, best_i)
        return best


    # Time: O(n**2), n = len(nums)
    # Space: O(n)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and length[i] < length[j] + 1:
                    length[i] = length[j] + 1

        return max(length)


    # Time: O(nlogn), n = len(nums)
    # Space: O(n)
    def lengthOfLIS2(self, nums):
        lst = []
        for num in nums:
            i = bisect.bisect_left(lst, num)
            if i == len(lst):
                lst.append(num)
            else:
                lst[i] = num

        return len(lst)


    def lengthOfLIS2WithPrint(self, nums):
        lst = []
        pos = []
        for num in nums:
            i = bisect.bisect_left(lst, num)
            if i == len(lst):
                lst.append(num)
            else:
                lst[i] = num
            pos.append(i)

        i = len(lst)-1
        for p in reversed(range(len(lst))):
            while pos[i] != p:
                i -= 1
            print(nums[i])

        return len(lst)

nums = [-7, 10, 9, 2, 3, 8, 8, 1, 4, 5, 1]
print(Solution().lengthOfLIS(nums))
print(Solution().lengthOfLIS2(nums))
nums=[]
print(Solution().lengthOfLIS(nums))
print(Solution().lengthOfLIS2(nums))
