import pylab

def findPayment(loan, r, m):
    """ 假设loan和r是浮点数，m是整数
        返回一个总额为loan，月利率为r，期限为m个月的抵押贷款的每月还款额 """
    return loan * ((r * (1+r)**m) / ((1+r)**m - 1))

class Mortgage(object):
    """ 用来建立不同种类抵押贷款的抽象类 """
    def __init__(self, loan, annRate, months):
        """ 假设loan和annRate为浮点数，month为整数
            创建一个总额为loan，期限为months，年利率为annRate的新抵押贷款 """
        self.loan = loan
        self.rate = annRate / 12
        self.months = months
        self.paid = [0.0] #每月已还款额
        self.outstanding = [loan] #每月剩余本金总额
        self.payment = findPayment(loan, self.rate, months) #每月还款额
        self.legend = None #贷款描述
    
    def makePayment(self):
        """ 记录支付每月还款额，计算剩余还款本金 """
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate #计算每月的还款本金
        self.outstanding.append(self.outstanding[-1] - reduction)
    
    def getTotalPaid(self):
        """ 返回至今为止的支付总额 """
        return sum(self.paid)

    def __str__(self):
        return self.legend

    # 绘图有关的函数
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)

    def plotTotPd(self, sytle):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, sytle, label = self.legend)
    
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * len(self.outstanding))
        equityAcquired = equityAcquired - pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)


class Fixed(Mortgage):
    """ 固定利率 """
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'
        #self.legend = 'Fixed, ' + str(r*100) + '%'
    
class FixedWithPts(Mortgage):
    """ 先支付贷款总额的pts%，剩下的部分可以享受低利率 """
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts/100)]
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, ' + str(pts) + ' points' 
        #self.legend = 'Fixed, ' + str(r*100) + '%, ' + str(pts) + ' points'
            

class TowRate(Mortgage):
    """ 前teaseMonths个月享受teaseRate利率（较低），然后享受r利率（较高） """
    def __init__(self, loan, r, months, teaseRate, teaseMonths):
        Mortgage.__init__(self, loan, teaseRate, months) #先用优惠期利率初始化对象
        self.teaseMonths = teaseMonths #优惠期月份
        self.teaseRate = teaseRate #优惠期利率
        self.nextRate = r / 12 #优惠期结束后的利率
        self.legend = str(teaseRate*100) \
            + '% for ' + str(self.teaseMonths) \
            + ' months, then ' + str(round(r*100, 2)) + '%'
        #self.legend = str(teaseRate*100) \
        #    + '% for ' + str(self.teaseMonths) \
        #    + ' months, then ' + str(r*100) + '%'
        
    def makePayment(self):
        if len(self.paid) == self.teaseMonths + 1: #优惠期结束后，使用优惠期后的利率计算利率和每月还款额，只会计算一次
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, 
                self.months - self.teaseMonths)
        Mortgage.makePayment(self) #调用父类记录还款额，计算剩余本金


def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    towRate = TowRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, towRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPaid())))
    plotMortgages(morts, amt)

def plotMortgages(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
    
    styles = ['k-', 'k-.', 'k:']
    payments, cost, balance, netCost = 0, 1, 2, 3 # 给图编号赋名
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
    
    labelPlot(payments, 'Monthly Payments of $' + str(amt) + 
        ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) + 'Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) + 
        'Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages', 'Months', 'Payments - Equity $')



""" 测试代码 """
compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25, ptsRate=0.05,
    varRate1=0.045, varRate2=0.095, varMonths=48)
pylab.show()
