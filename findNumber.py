from random import randint
from time import time

t1 = time()

# Function to perform binary search
def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Function to check whether any pair exists
# whose sum is equal to the given target value
def twoSum(arr, target):
    arr.sort()

    # Iterate through each element in the array
    for i in range(len(arr)):
        complementation = target - arr[i]

        # Use binary search to find the complementation
        if binary_search(arr, i + 1, len(arr) - 1, complementation):
            return True
    # If no pair is found
    return False


# create a random array(list) for test functions
nums = [randint(0, 1000000) for _ in range(1000000)]

print(twoSum(nums, 701))

# measure time
print(time() - t1)
