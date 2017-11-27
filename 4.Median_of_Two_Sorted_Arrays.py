class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1

        k = (n1 + n2 + 1) // 2
        lo, hi = 0, n1
        while lo < hi:
            m1 = (lo + hi) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                lo = m1 + 1
            else:
                hi = m1

        m1, m2 = lo, k - lo
        lmax = max(float('-inf') if m1 == 0 else nums1[m1-1],
                   float('-inf') if m2 == 0 else nums2[m2-1])
        if (n1 + n2) % 2 == 1:
            return lmax
        rmin = min(float('inf') if m1 == n1 else nums1[m1],
                   float('inf') if m2 == n2 else nums2[m2])

        return (lmax + rmin) * 0.5

def test(nums1, nums2, e):
    r = Solution().findMedianSortedArrays(nums1, nums2)
    print(e == r, e, r)

test([1,2], [3], 2)
test([1,3], [2], 2)
test([1], [2,3], 2)
