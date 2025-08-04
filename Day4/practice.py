#Tuples
''' 
allows duplicates
immutable
ordered
creating a tuple
'''
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)
# index = tuple1.index(3)
# count = tuple1.count(2)
# print("index of 3:", index)
# print(count)
# length = len(tuple1)
# print(length)
# max_value = max(tuple1)
# print(max_value)
# min_value = min(tuple1)
# print(min_value)
# addition = sum(tuple1)
# print(addition)

# list=["shreya", "1"]
# parapa = tuple(list)
# print(parapa)
# print(type(list))
# print(type(parapa))

#DSA PROBLEM
# my_tuple=(10,20,30,10,50,10)
# target=20

# index_of_10 = my_tuple.index(10)
tuple1=(10,20,30,10,10,40)
target=10
indexes=[]
for i in range(len(tuple1)):
  if tuple1==target:
    indexes.append(i)
print(indexes)