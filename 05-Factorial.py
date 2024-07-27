
#!WAP to factorial to function 
# def fact(n):
#     if n<0:
#         return "it is n ot exist"
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))    

#! WAP to factorial using Loop
num=int(input("Enter the number :"))
fact=1
if num<0:
    print("Factorial 0 is not exist")
    
if num==1:
       print("Factorial 1 is 1") 
        
if num>1:
      for i in range(1,num+1):
            fact=fact*i
            
print(fact)              