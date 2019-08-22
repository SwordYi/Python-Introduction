class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsovisible__ = 'Look at me too'
        self.__invisible = 'Don\'t loo at me directly'
    
    def printVisible(self):
        print(self.visible)
    
    def printInvisible(self):
        print(self.__invisible)

    def __printInvisible(self):
        print(self.__invisible)
    
    def __printInvisible__(self):
        print(self.__invisible)
    

test = infoHiding()
print(test.visible)
print(test.__alsovisible__)
test.printVisible()
test.printInvisible()
test.__printInvisible__()
try:
    test.__invisible
except AttributeError as msg:
    print(msg)
try:
    test.__printInvisible()
except AttributeError as msg:
    print(msg)
