import IntSet

print(type(IntSet.IntSet), type(IntSet.IntSet.insert))

s = IntSet.IntSet()
s.insert(3)
s.insert(4)
s.insert(10)
print(s.member(3))
print(s.member(2))
print(s)
print(s.getMembers())
s.remove(10)
print(s)
print(s.remove(2))