from random import randint
from time import time

t1 = time()

# Function to check whether any pair exists
# whose sum is equal to the given target value


def twoSum(arr, target):

    # Create a set to store the elements
    s = set()

    # Iterate through each element in the array
    for num in arr:

        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False


# create a random array(list) for test functions
nums = [randint(0, 1000000) for _ in range(1000000)]

# call the function and print result
print(twoSum(nums, 701))

# measure time
print(time() - t1)
