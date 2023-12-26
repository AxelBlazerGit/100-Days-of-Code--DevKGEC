one=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
two=["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
misc=["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
def words(n):
    word=''
    if n>=1000:
        word+=one[n//1000] + " thousand "
        n %= 1000
    if n>=100:
        word+=one[n//100] + " hundred "
        n %= 100
    if n>0:
        if n>=20:
            word+=two[n//10]
            n %= 10
        elif n>=11:
            word+=misc[n-10]
            n=0
        if n>0:
            word+=' '+one[n]
    return word.strip()
number=int(input("Enter a number(up to 4 digits): "))
print(words(number))
