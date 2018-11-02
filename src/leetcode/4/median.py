class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        composite = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                composite.append(nums1[i])
                i += 1
            else:
                composite.append(nums2[j])
                j += 1

        composite += nums1[i:]
        composite += nums2[j:]

        median = len(composite) // 2

        if len(composite) % 2 == 0:
            # even number of items
            median = (composite[median-1] + composite[median]) / 2
            return median
        else:
            # odd number of items
            median = composite[median]
            return median
