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

print(genPowerset([1, 2, 3, 'x']))

    