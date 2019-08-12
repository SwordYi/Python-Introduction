nameHandle = open('4_6_1_kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('4_6_1_kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()