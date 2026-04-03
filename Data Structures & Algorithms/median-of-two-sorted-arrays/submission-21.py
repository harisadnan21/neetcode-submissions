class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # should be a comb if sum of lens is even
        # if total is odd, chose the bigger of A_left, B_left
        # if even, return (max(A_left, B_left) + min(A_right, B_right))/2

        A = nums1
        B = nums2
        total_len= len(A)+ len(B)
        half_idx = total_len //2
        

        if len(A) > len(B):
            A, B = B, A

        A_start = 0
        A_end = len(A) - 1
        while True:

            i = (A_start + A_end) // 2
            j = half_idx - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                break
            elif Aleft > Bright:
                #shift A left
                A_end = i - 1

            elif Bleft > Aright:
                #shift A right
                A_start = i + 1
            
        if total_len %2 == 0 :
            return (max(Aleft, Bleft) + min(Aright, Bright))/2
        return min(Aright, Bright)
        
        