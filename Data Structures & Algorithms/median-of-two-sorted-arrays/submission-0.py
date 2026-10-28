class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B  = nums1, nums2 # rename given arrays
        total = len(nums1)+len(nums2) # total length of both arrays
        half = total // 2 # half of total length

        if len(B)<len(A): # perform binary search on A; check if A is array with smallest length, if not, swap A, B
            A,B = B,A

        l, r = 0, len(A)-1 # left and right pointers
        while True:
            i = (l+r) // 2 # index of A
            j = half-i-2 # index of B

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if (i+1)<len(A) else float('infinity')
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1)<len(B) else float('infinity')

            # verify if the partition is right
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft,Bleft) + min(Aright,Bright))/2
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1