
myDict = {"name":"ali", "Family":"Rezaie", 12:"aryan"}
print(myDict)
print(len(myDict))
print(list(myDict))

myDictKeys = myDict.keys()
print(myDictKeys)

myDictValues = myDict.values()
print(myDictValues)

myDictItems = myDict.items()
print(myDictItems)

myDictKeysList = list(myDictKeys)
print(myDictKeysList)

myDictValuesTuple = tuple(myDictValues)
print(myDictValuesTuple)

students = {110:{"name":"Aryan", "family":"Rohani", "grade":[11,12.5,13,15]},
            115:{"name":"ali", "family":"ahmadi", "grade":[14,6.5,19,17]},
            120:{"name":"mehdi", "family":"amiri", "grade":[18,11,16.5,11.5]}}
print(students[115]["name"])
print(students[115]["grade"])


m = {1,2,3,4,5,6}
print(m)
print(type(m))
#print(m[2])
#m[2] = 12
m = {1,2,6,3,2,1,4,5,1}
print(m)
c = { "reza", "ali", "majid", "Ahoora"}
print(c)
name = "aryan"
l1 = name
name = set(name)
print(name)
l1 = list(l1)
print(l1)
list1= [10,25,35,10,15,0,13,-16,19,25,0]
mySet = set(list1)
print(mySet)
myList = list(mySet)
myList.sort()
myList.reverse()
print(myList)



myRange = range(0,10,1)
print(myRange)
myList = list(myRange)
print(myList)

myTuple = tuple(myRange)
print(myTuple)
