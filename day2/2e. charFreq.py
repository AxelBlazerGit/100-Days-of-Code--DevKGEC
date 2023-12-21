charFreq={}
str=input("enter a sentence to obtain character frequency: ")
for char in str:
    if char in charFreq:
        charFreq[char]+=1
    else:
        charFreq[char]=1
for char in charFreq:
    print(f"\nFrequency of  {char} in {str} = {charFreq[char]}")