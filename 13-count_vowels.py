
sentence=input("enter the sentence :")
str=sentence.lower()

count=0

list=["a","e","i","o","u"]

for char in str:
    if char in list:
        count=count+1
print("int sentence vowels are :",count)        