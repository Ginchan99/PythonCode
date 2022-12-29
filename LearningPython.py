#This is our first lesson in Python

#Variable Declaration
someNumber = 1
print(someNumber)
print('someNumber = ', someNumber) #string

#Variable Declaration String
print('-'*50)
name = 'Tushti'
print("My name is: ", name)
print('-'*50)

#Simple For Loop - Type all nos from 1 to 10
print('-'*50)
for num in range(10):
    print(num+1)
print('-'*50)

#Print only even integers from 1 to 10
print('-'*50)
for num in range(10):
    remBy2 = num %2
    #print("num =", num)
    #print("remBy2=", remBy2)
#Now we will use If function to determine only even values
    if(remBy2==1):
       print(num+1)

print('-'*50)
#if using a function
# using if function to determine whether even or odd


def isEven(num):
    remBy2 = num %2
    if remBy2 == 1:
        return False
    else:
        return True

print('-'*50)
for num in range(10):
    if isEven(num+1):
        print(num+1)
print('-'*50)

#%%
