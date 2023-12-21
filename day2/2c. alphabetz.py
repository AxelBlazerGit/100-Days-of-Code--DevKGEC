def count(st):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vCount,cCount=0, 0

    for char in st:
        if char in vowels:
            vCount+=1
        elif char in consonants:
            cCount+=1
    return vCount,cCount
vowels,consonants=count(input("Enter a string: "))
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
