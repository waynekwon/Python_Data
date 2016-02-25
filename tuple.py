classmates=('Michael','Bob','Tracy')
print(type(classmates))
print(classmates)

#you can't change 'tuple'
#classmates.append('Mark')


t=(1,2)
print(type(t))
print(t)
#this is an interger
t=(1)
print(type(t))
print(t)
#need to add comma
t=(1,)
print(type(t))
print(t)

#tuple can't be changed, but the list inside a tuple can be changed
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)
