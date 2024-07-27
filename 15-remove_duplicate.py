
#!remove the duplicate value in sentence
sentence=input("Enter the Sentence- ")
l=[ ]

for char in sentence:
    if char not in l:
        l.append(char)

op=''.join(l)
print(op)    
