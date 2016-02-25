classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))

#starting from 0
print(classmates[0])
print(classmates[-1])

#if you don't know how long the list is
print(classmates[len(classmates)-1])

print(type(len(classmates)))

#adding elements to list
classmates.append('Wayne')
print(classmates)

classmates.insert(1,'Mark')
print(classmates)

#deleting
classmates.pop()
print(classmates)

#this will print what has been 'popped' out of the list
print(classmates.pop())
print(classmates)

print(classmates.pop(1))
print(classmates)

#changing the values
classmates[1]='Wayne'
print(classmates)

s=['python','java',['asp',[1, True, 'February'],'php'],'scheme']

print(s[2])
print(s[2][1])
print(s[2][1][2])

#starting with empty list
L=[]
L.append('Apple')
print(L)
L[0]='Google'
print(L)

#exercise
List=[['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
#print apple
print(List[0][0])
#print Python
print(List[1][1])
#print Lisa
print(List[2][2])


#adding
new_class=classmates+['Jake','Peter']
print(new_class)

#replacing - starts at the first number, and before the second number
new_class[1:3]=[]
print(new_class)

#removing without knowing the position
new_class.remove('Michael')
print(new_class)

#reverse
print(classmates)
classmates.reverse()
print(classmates)

#adding to the list
last=[x+' LastName' for x in classmates]
print(last)

#adding numbers
number=[1,2,3,4,5,6,7]
number_add=[x+1 for x in number]
print(number_add)

#making list with 'range'
numbers=list(range(1,101))
print(numbers)

#square of each number
numbers_sqr=[(x**2) for x in numbers]
print(numbers_sqr)