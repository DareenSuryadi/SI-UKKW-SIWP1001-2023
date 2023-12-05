# """
# Diberikan sebuah array berisi integer nums yang telah diurutkan secara ascending, 
# serta sebuah integer target, tuliskan sebuah fungsi untuk mencari target di dalam nums. 
# Jika target ada, maka kembalikan indeksnya. Jika tidak, kembalikan -1.

# algorithma binarySearch harus mencapai O(log n) runtime complexity.

# Contoh 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Penjelasan: 9 ada di nums dan indeksnya adalah 4

# Contoh 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Penjelasan: 2 tidak ada di nums jadi kembalikan -1

# Batasan:
# 1 <= panjang nums <= 10^4
# -10^4 < nums[i], target < 10^4
# semua angka harus integer unik
# semua angka di urutkan secara ascending

# """
from typing import List
from util.decorators import time_decorator
@time_decorator

class BS():
    def __init__(self,nums,target) -> None:
        nums = self.nums
        target = self.target

def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


