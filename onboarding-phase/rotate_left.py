def rotateLeft(d, arr):
    length = len(arr)
    ans = [0] * length
    
    for i in range(length):
        ans[i - d] = arr[i]
    return ans
        
