str=input("Enter something random: ")
result=""

for ele in str:
    ascii=ord(ele)
    if (not (65<=ascii<=90) and not (97<=ascii<=119) and not (48<=ascii<=57)):
        result += ele

print(result)
