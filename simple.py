
#List
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)
thislist.remove("banana")
print(thislist)



sora = ["apple", "banana",3,9.0872, "cherry"]
print(sora)

#sora.sort()#1
#

sora.append("orange")#2
print(sora)

sora.insert(1,"cherry")#3
print(sora)

#Method count, pop, sort,clear,remove,reverse,insert,
sora.pop(1)#4
print(sora)

sora.reverse()#5
print(sora)
#
#

a = [1, 2, 3]
b = [4, 5]
a.extend(b)#8
print(a)


#Dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)#1


x=car.get("brand")
print(x)#2

x=car.keys()
print(x)#3

car.update({"color": "White"})
print(car)#4


car.clear
print(car)

