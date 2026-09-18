# print number from 1 to 20
'''for i in range(1,21):
    print(i)'''

#print even number from 1 to 50
'''for i in range(0,50):
    if i%2==0:
        print(i)
    else:
        print(i,"is odd number")   '''

#sum of numbers from 1 to 100 using loops
'''sum=0
for i in range(1,101): 
    sum=sum+i
    print(sum)'''

#multiplication table
'''num=int(input("enter a number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)'''
#Count digits using for loop
num = input("Enter a number: ")
count = 0
for digit in num:
    count = count + 1
    print("Number of digits =", count)