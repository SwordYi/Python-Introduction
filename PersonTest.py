from Person import Person
import datetime

me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
print(her.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')
print(her < me)

pList = [me, him, her]
for p in pList:
    print(p)
pList.sort()
for p in pList:
    print(p)

