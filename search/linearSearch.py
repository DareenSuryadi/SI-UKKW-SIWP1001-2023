"""
Buat sebuah algorithm LinearSeach

definisikan linear search terlebih dahulu 
lalu buat fungsi untuk mencari target 
tuliskan sebuah fungsi untuk mencari target di dalam nums. 
Jika target ada, maka kembalikan indeksnya. Jika tidak, kembalikan -1.

"""
from typing import List
from util.decorators import time_decorator
@time_decorator

class LS():
    def __init__(self,arr,target) -> None:
        arr = self.arr
        target = self.target

@time_decorator
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

   
   
numbers = [4, 2, 5, 1, 7, 3, 6, 8]
target = 5    

result = linear_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")

numbers = [4, 2, 5, 1, 7, 3, 6, 8]
target = 9

result = linear_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")
    pass