class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result

def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0 / item.getWeight
def density(item):
    return item.getValue() / item.getWeight()

# 建立对象
def buildItems():
    names = ['clock','painting','radio','vase','book','computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction) 
    print('Total value of items taken is', val)
    for item in taken:
        print(' ', item)

# 暴力寻找最优解
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)


def getBinaryRep(n, numDigits):
    """ 假设n和numDigits为非负整数，
        返回一个长度为numDigits的字符串，为n的二进制表示 """
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enouth digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerset(L):
    """ 假设L是列表，
        返回一个列表，包含L中元素所有可能的子集。
        例如，如果L=[1, 2]，则返回的列表包含元素[]、[1]、[2]和[1, 2] """
    powerset = []
    for i in range(0, 2**len(L)): #一个列表的所有可能子集是2的列表长度的指数次方
        #很巧妙的做法，将所有可能子集数量转换回二进制，和列表的长度对齐，然后再取1的位置的元素即为一个子集
        binStr = getBinaryRep(i, len(L)) 
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

# 测试代码   
def testchooseBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)

testchooseBest()