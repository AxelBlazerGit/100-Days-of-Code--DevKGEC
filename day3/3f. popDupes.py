def popDupes(arr):
    arr2=[]
    for ele in arr:
        if ele in arr2:
            continue
        else:
            arr2.append(ele)
    return arr2
print(popDupes(list(input("enter array: ").split())))