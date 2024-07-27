# num=int(input("Enter the number :"))

# if num==1:
#     print("it is not a prime number")
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("it is not a prime number")
#             break
#     else:
#       print("it is the prime number")




num=int(input("Enter the number"))

if num==1:
    print("not prime")
if num>1:
    for i in range(2,num):
       if num%i==0:
           print("not a prime")
           break
    else:
        print("prime number")       

 