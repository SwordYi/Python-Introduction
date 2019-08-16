from MITPerson import MITPerson, Student, UG, Grad
from Person import Person

p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

p2 = MITPerson('Mark Guttag')
p3 = MITPerson('Billy Bob Beaver')
p4 = MITPerson('Billy Bob Beaver')
p5 = Person('Billy Bob Beaver')
print(str(p2) + '\'s id number is ' + str(p2.getIdNum()))
print(str(p3) + '\'s id number is ' + str(p3.getIdNum()))
print(str(p4) + '\'s id number is ' + str(p4.getIdNum()))
print(MITPerson.nextIdNum)
print('p1 < p2 =', p1 < p2)
print('p3 < p2 =', p3 < p2)
print('p4 < p1 =', p4 < p1)

print('p5 < p1 =', p5 < p1)
print('p5 < p2 =', p5 < p2)

p6 = UG("Sword", 2019)
print(str(p6) + '\'s id number is ' + str(p6.getIdNum()))
print(MITPerson.nextIdNum)
print(UG.nextIdNum)
print(p4, 'is a student is', p4.isStudent())
print(p6, 'is a student is', p6.isStudent())