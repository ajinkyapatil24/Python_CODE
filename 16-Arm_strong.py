
n=int(input("Enter the number :"))

temp=n
sum=0

while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n//10

if temp==sum:
    print("Arm strong number")
else:
    print("not arm strong number")    
