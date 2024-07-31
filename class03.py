a = [10, 20, 30]
print(a)
# [10, 20, 30]
print(type(a))
#<class 'list'>
print(a[0])
# 10
print(a[2])
# 30
# print(a[3])
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     print(a[3])
# IndexError: list index out of range
a[0]=12.5
print(a)
# [12.5, 20, 30]
a[1]=16
print(a)
# [12.5, 16, 30]
a[0] = "Arian"
print(a)
# ['Arian', 16, 30]
a[2]= True
print(a)
# ['Arian', 16, True]
a = [10,15.5, False, "Aryan", None]
print(a[1])
15.5
print(type(a[2]))
# <class 'bool'>
b = [1,2,3,[4,5,6],7,[8,9]]
print(len(a))
# 5
print(len(b))
# 6
x = b[3]
print(x)
# [4, 5, 6]
print(x[0])
# 4
# print(a[5][0])
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     print(a[5][0])
# IndexError: list index out of range
print(b[5][0])

b = [1,2,3,[4,["A","bb","t"],6],7,[8,9]]
print(b[3][1][2])

a = "Aryan"
print(a[0])

print(a[2])

# a[0] = "K"
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     a[0] = "K"
# TypeError: 'str' object does not support item assignment
a = [1,2,3,4]
# a = int(a)
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     a = int(a)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a = bool(a)
print(a)
# True
a = []
a = bool(a)
print(a)
# False
a = [1,2,3,4,5]
a = str(a)

print(a)
# [1, 2, 3, 4, 5]
print(a[0])

print(a[2])

print(a[3])
 
print(a[4])

print(a[1])

a = "aryan"
a = list(a)
print(a)
# ['a', 'r', 'y', 'a', 'n']
print(a[0])
# a
print(a[4])
# n