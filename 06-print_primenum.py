 
#!print the prime number 1 to 100
# for num in range(1,100):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num) 




num=int(input("enter the number"))

for num2 in range(1,num):
 if num2>1:
  for i in range(2,num2):
    if num2% i==0:
     break
  else:
    print(num2)