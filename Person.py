import datetime

class Person(object):
    def __init__(self, name):
        """ 创建一个人 """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        """ 返回self的全名 """
        return self.name
    
    def getLastName(self):
        """ 返回self的姓 """
        return self.lastName
    
    def setBirthday(self, birthday):
        """ 假设birthday是datetime.date类型 
            将self的生日设置为birthday """
        self.birthday = birthday
    
    def getAge(self):
        """ 返回self的当前年龄，用日表示 """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """ 如果self按字母顺序位于other之前，则返回True，否则返回False
            首先按照姓进行比较，如果姓相同，就按照全名比较 """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """ 返回self的全名 """
        return self.name
