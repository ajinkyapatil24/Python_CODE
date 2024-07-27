
# #! Increasing Triangle Pattern
# n=int(input("Enter the number :"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()  

# #! Decreasing Triangle Pattern
# n=int(input("Enter the number :"))
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()         

#!Hill Triangle Pattern
n=5
for i in range(n):
    for j in range(i+1):
        print("",end=" ")

    for j in range(i,n-1):
        print("*",end=" ")
        

    for j in range(i,n):
        print("*",end=" ")    
    print()    