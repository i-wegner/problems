# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


# immediate solution idea is O(n^2)
# traverse the list, comparing all elements and check if they sum to the target
    # solved with a list - should be array (per problem wording)
def twoSum(nums, target):
    solution = False
    i = 0
    for element in nums:
        for j in range(1, len(nums)):
            if element + nums[j] == target:
                indices = [i, j]
                return indices
        i += 1

    if solution == False:
        print("No solution within the given array.")