def revArr(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    print(arr)

revArr(list(input("enter an array of numbers: ")))

