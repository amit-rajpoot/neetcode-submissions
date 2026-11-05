class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Step 1: Binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        # Step 2: Binary search boundaries
        low = 0
        high = n

        while low <= high:

            # Step 3: Find partition positions
            i = (low + high) // 2
            j = (n + m + 1) // 2 - i

            # Step 4: Find four boundary values
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == n else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == m else nums2[j]

            # Step 5: Check correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total elements
                if (n + m) % 2 == 1:
                    return max(left1, left2)

                # Even total elements
                return (max(left1, left2) +
                        min(right1, right2)) / 2

            # Step 6: Move binary search left
            elif left1 > right2:
                high = i - 1

            # Step 7: Move binary search right
            else:
                low = i + 1