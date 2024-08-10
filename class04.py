myTuple = (1,2,3,4,5,6)
print(type(myTuple))
print(myTuple)
print(myTuple[4])
#myTuple[4]=55
x = myTuple[1:4:2]
print(x)
s = str(myTuple)
print(s)
b = bool(myTuple)
print(b)
myList = list(myTuple)
print(myList)
myList[4]=55
print(myList)
myTuple = tuple(myList)
print(myTuple)
l1 = [1,2,3,3,2,1,1]
print(l1)
t1 = (1,2,2,3,1,2,1)
print(t1)
t2 = (1,2,(3,4,5),6,(7))
print(t2)
print(len(t2))
print(t2[2][1])


a = b = 10
print(a)
print(b)
a = b = c = 15
print(a)
print(c)

x,y = 10, 12
print(x)
print(y)

#x,y = 10, 12 , 15
#print(x)

x = 10, 20, 30
print(x)
print(type(x))



myDict = {"name" : "Aryan", "age":21}
print(myDict)
print(type(myDict))

d1 = {"name" : "Aryan", "age" : 21 , "avg" : 15.5, "Status" : True, "grade" : [10,11,12.5,9.5,14.5], "favorite" : ("sport", "Language", "Programming"), 110:"Police", 0:None, 5>2 : "Ok"}
print(d1)
print(d1["grade"])
print(d1[110])
print(d1[True])

d2={"name": "arian", "family": "Rohani", "name":"Ahoora", "name" : "Matin", "family": "Sharifi"}
print(d2)

#list3 = int(d2)
b = tuple(d2)
print(b)

c = list(d2)
print(c)

s = str(d2)
print(s)
