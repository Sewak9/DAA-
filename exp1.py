import random 
import time
import sys
def interpolation_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= x <= arr[right]:
        if arr[left] == arr[right]:
            return left if arr[left] == x else -1
        
        pos = left + int((x - arr[left]) / (arr[right] - arr[left]) * (right - left))
        
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


# Test
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(interpolation_search(arr, 60))  
print(interpolation_search(arr, 90))
