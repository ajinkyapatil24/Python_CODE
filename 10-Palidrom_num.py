
n=int(input("Enter the number :"))

temp=n
sum=0

while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if temp==sum:
    print("pali")
else:
    print("not pali")    
