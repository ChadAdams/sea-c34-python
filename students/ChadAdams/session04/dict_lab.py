
"""Task #1"""
print "Task #1"
print ""
cake_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print "My dictionary:", cake_dict
cake_dict.pop('cake')
print "Cake item has been removed:", cake_dict
cake_dict['fruit'] = 'Mango'
print "Fruit item has been added:", cake_dict
print "Dictionary keys:", cake_dict.keys()
print "Dictionary values:", cake_dict.values()
print "Is cake a valid item in the Dictionary?",'cake' in cake_dict
print "Is Mango a valid value in the Dictionary?", 'Mango' in cake_dict.values()
print ""

"""Task #2"""
print "Task #2"
print ""
list1 = []
list2 = []
new_dict = {}
for i in range(16):
    list1.append(i)
    list2.append(hex(i))

for i, j in zip(list1, list2):
   new_dict[i] = j

print "Number list:", list1
print "Hex list:", list2
print "Dictionary:", new_dict
print ""

print "Task #3"
print ""
print "The dictionary from Task 1:", cake_dict
for key, val in cake_dict.items():
    cake_dict[key] = val.count('a')

print "The values have been replaced with A's:", cake_dict
print ""
print "Task #4"
print ""
s2 = set()
s3 = set()
s4 = set()
for i in range(0,21,2):
    s2.add(i)

for i in range(0,21,3):
    s3.add(i)

for i in range(0,21,4):
    s4.add(i)

print "Numbers divisible by 2:", s2
print "Numbers divisible by 3:", s3
print "Numbers divisible by 4:", s4

print "Is s3 a subset of s2?", s3.issubset(s2)
print "Is s4 a subset of s2?", s4.issubset(s2)
print ""
print "Task 5"
print ""
p_set = set('Python')
p_set.add('i')
print "This set contains the word python and the letter i:", p_set
fro_set = frozenset('marathon')
print "This is a frozenset that contains the word marathon:", fro_set
print "The intersection of these sets is:", p_set.intersection(fro_set)
print "The union of these sets is:", p_set.union(fro_set)
