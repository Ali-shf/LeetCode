

# Brute force --> O(n ^ 2)
def two_sum(nums: list, target: int) -> list:
    is_found = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                is_found = True
                return [i, j]
    if is_found == False:
        return "not found"
    
# hash table --> O(1) (constant time) and worse case --> O(n)


def two_sum(nums: list, target: int) -> list:
    seen = {} # hash table in python
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i







