Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    
    
# Get the DNA string from the user
s= input("Enter a DNA string: ")

# Initialize counters for each symbol
a = 0
c = 0
g = 0
t = 0

# Loop through each symbol in the DNA string and update the corresponding counter
for symbol in s:
    if symbol == 'A':
        a += 1
    elif symbol == 'C':
        c += 1
    elif symbol == 'G':
        g += 1
    elif symbol == 'T':
        t += 1

# Print the counts
print(a, c, g, t)
