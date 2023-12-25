def targetIndices(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if int(nums[i]) + int(nums[j]) == target:
                return [i, j]
    return None
result=targetIndices(list(input("Enter numbers into array: ").split()), int(input("Enter target sum: ")))

if (result is not None):
    print(f"The indices are: {result[0]} and {result[1]}")
else:
    print("No solution found.")
