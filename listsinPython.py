#first we import all the packages

import numpy as np

#1 Create a list
listofNos = list(range(10))
print("listofNos=", listofNos)

#create list with alternative nos
#listofNos = list(range(startno,lastno,gap))
listofNos = list(range(1,10,2))
print("listofNos=", listofNos)

#create list of even nos below 10 in reverse
listofNos = list(range(10,1,-2))
print("listofNos=", listofNos)

#can we iterate through the list and print the nos if its a multiple of 3?
listofNos = list(range(1,100,1))
#adding the list at the end of original
listofmulof3 = []
for num in listofNos:
    if num % 3 == 0:
        listofmulof3.append(num)

print("listofmulof3=",listofmulof3)

#get multiples of 3 and 5
listofmulof3 = list(range(3,100,3))
listofmulof5 = list(range(5,100,5))
print("listofmulof3=",listofmulof3,"listofmulof5=",listofmulof5)
listofmulof3and5 = []
for num in listofmulof3:
    if num in listofmulof5:
        listofmulof3and5.append(num)
print("listofmulof3and5=",listofmulof3and5)

#get multiples of 3 or 5, merging them
listofmulof3or5 = listofmulof3+listofmulof5
print("listofmulof3or5=",listofmulof3+listofmulof5)
sortedlistofmulof3or5 = sorted(listofmulof3or5)
print("sortedlistofmulof3or5=",sortedlistofmulof3or5)

#remove duplicates from the list
deduplicatedlist = []
for numIndex in range(1,len(sortedlistofmulof3or5),1):
    num = sortedlistofmulof3or5[numIndex-1]
    next_num = sortedlistofmulof3or5[numIndex]
    if num!= next_num:
        deduplicatedlist.append(num)

print("deduplicatedlist=",deduplicatedlist)
#faster method to remove duplicates
print("fastduplicatedlist=",list(set(sortedlistofmulof3or5)))


listofwords = ["rahul","prateek","tushti","rohit"]
print("meenakshi" in listofwords)
print("prateek" in listofwords)
