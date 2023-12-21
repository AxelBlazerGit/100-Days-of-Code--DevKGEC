def fiboRecurse(n, sequence=[0, 1]):
    if n<=len(sequence):
        return sequence[:n]
    sequence.append(sequence[-1] + sequence[-2])
    return fiboRecurse(n, sequence)
n = int(input("Enter the value of n: "))
sequence = fiboRecurse(n)
print(f"Fibonacci sequence up to the {n}th term: {sequence}")
