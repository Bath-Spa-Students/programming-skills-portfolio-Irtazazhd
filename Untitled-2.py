
'''
x = 100
y = 200 
z = 300
print('x' , end = ' = ')
print('y' , end = ' = ')
print('z ')
'''
'''
name1  = 'irti'
name2 = 'abdu'
name3 = 'topper'
print('my name is',name1)
print('my name is',name2)
print('my name is',name3)
'''
'''
name = 'irti'
country = 'pakistan'
age = '16'
print('my name is', name )
print('i live in' , country )
print(f'my age is', age )
'''

'''
name = 'irti'
age = '16'
country ='pakistan'
#print(f'my name is', name , 'my age is', age, 'and i live in', country)

name = 'topper'
age = '18'
harami = 'infinite'
print(f'my name is', name, 'my age is', age, 'i am so harami', harami)
'''
'''
x = 20
print(type (x))

x = 20.10
print(type (x))

x = '20'
print(type (x))

x = 20 + 10j
print(type (x))
'''
'''
y = false
print(type(y))
'''
'''
x = 'irti cand cafetaria'
print(x[12])

x = 'irti cand cafetaria'
print(x[-12])
'''
'''
x = 'irti cand cafetaria'
print(len(x))
'''
'''
x = 'irti and cafetaria'
print(x[0:14])
'''

# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Removing all occurrences of 20
list1 = [item for item in list1 if item != 20]

# Result
print(list1)