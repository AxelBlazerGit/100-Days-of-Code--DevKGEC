def commons(list1, list2):
    common=[]
    for ele1 in list1:
        for ele2 in list2:
            if ele1==ele2:
                common.append(ele1)
                break
    return common
result=commons(list(input("enter first array: ").split()),list(input("enter second array: ").split()))
print("Common elements:", result)
