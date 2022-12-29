#1. Write a simple program with 2 for loops to print all prime numbers between 1 and 100
#2. Write a function that takes 2 inputs, (num1, num2) and outputs whether num1 is divisible by num2.
#3. Write a function that takes 3 inputs, (num1, num2, num3) and outputs num1*num2*num3.
#4. Write a function that takes 2 inputs, (num1, num2) and whether num1 > num2 or not.
#4. Write a function that takes 2 inputs, (num1, num2) and outputs the greater of num1 and num2.

#Prime No
print('-'*50)
def is_prime(num):
    for i in range(2,num):
        if (num%i) == 0:
            return False
    return True
 print('-'*50)

print('-'*50)
for num in range(100):
    if is_prime(num+1):
        print(num+1)
print('-'*50)

#Whether num1 is divisible by num2.
print('-'*50)
def is_div(i1,i2):
        if i1 % i2 == 0:
            return True
        else:
            return False

print(is_div(45,5))
print(is_div(7,6))

print('-'*50)

#n1*n2*n3
print('-'*50)
def mul(n1,n2,n3):
    return n1*n2*n3

print(mul(87,45,5))
print(mul(41,7,6))

print('-'*50)

#whether n1>n2 or not?
print('-'*50)
def n1isgreater(n1,n2):
    if (n1>n2):
        return True
    else:
        return False

print(n1isgreater(45,5))
print(n1isgreater(12,74))

print('-'*50)


#Printing the greater no
print('-'*50)
def is_more(n1,n2):
    if (n1>n2):
        return n1
    else:
        return n2
print(is_more(7,8))
print(is_more(65,51))

print('-'*50)

