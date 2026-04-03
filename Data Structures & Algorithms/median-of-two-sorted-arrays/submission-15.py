from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2   # <-- LEFT gets the extra element if odd

        l, r = 0, len(A)

        while True:
            i = (l + r) // 2
            j = half - i

            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < len(A) else float("inf")

            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < len(B) else float("inf")

            # valid partition
            if A_left <= B_right and B_left <= A_right:
                # odd → median is max(left)
                if total % 2 == 1:
                    return max(A_left, B_left)

                # even → average of middle two
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1