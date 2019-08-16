class  IntSet(object):
    """ IntSet是一个整数集合 """
    # 关于实现（不是抽象）的信息：
    # 集合的值由一个整数数组self.vals表示。
    # 集合中的每个整数在self.vals中只出现一次。

    def __init__(self):
        """ 创建一个空的整数集合 """
        self.vals = []

    def insert(self, e):
        """ 假设e是整数，将e插入self """
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ 假设e是整数，如果e在self中，则返回True，否则返回False """
        return e in self.vals
    
    def remove(self, e):
        """ 假设e是整数，从self中删除e
            如果e不在self中，则抛出ValueError异常 """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """ 返回一个包含self中元素的列表，对元素不进行排序 """
        return self.vals[:]

    def __str__(self):
        """ 返回一个表示self的字符串 """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' # -1可以忽略最后的逗号
