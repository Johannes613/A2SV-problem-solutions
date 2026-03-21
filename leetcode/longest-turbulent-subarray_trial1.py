class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2: return 1
        max_sum = 1
        curr_sum = 2
        n = len(arr)
        
        if arr[0] > arr[1]: chg = 1
        elif arr[0] < arr[1]: chg = 0
        else: chg = -1


        for i in range(n-1):
            if arr[i] == arr[i + 1]:
                curr_sum = 1
                chg = -1
            elif arr[i] > arr[i + 1] and chg == 0:
                curr_sum += 1
                chg = 1
            elif arr[i] < arr[i + 1] and chg == 1:
                curr_sum += 1
                chg = 0
            else:
                curr_sum = 2
                if arr[i] > arr[i + 1]: chg = 1
                else: chg = 0    

            max_sum = max(max_sum , curr_sum)

        return max_sum 
                

        