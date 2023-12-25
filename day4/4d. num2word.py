one=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten"]
two=["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
misc=["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
def words(n):
    word=''
    if n>19:
        word+=one[n%10]
        n//=10
        word=two[n%10]+' '+word
        n//=10
        if n>0:
            word=one[n%10]+' hundred '+word
        n//=10
        if n>0:
            word=one[n%10]+" thousand "+word
    elif n<11:
        return one[n]
    else: 
        return misc[n-10]
    return word;
print(words(int(input("Enter a no(up to 4 digits): "))))