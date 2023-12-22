def concatenate_arrays(arr1, arr2):
    len1=len(arr1)
    len2=len(arr2)
    result=[]
    for i in range(len1):
        result.append(arr1[i])
    for j in range(len2):
        result.append(arr2[j])
    return result
concatenated_array=concatenate_arrays(list(input("Enter first array: ").split()), list(input("Enter second array: ").split()))
print("Concatenated Array:", concatenated_array)
