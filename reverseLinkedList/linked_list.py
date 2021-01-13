from node import Node
class LinkedList:
    def __init__(self):
        self.headValue = None

    def insert(self, value):
        element = Node(value)
        if self.headValue is None:
            self.headValue = element
        else:
            tempValue = self.headValue
            while tempValue.getNextValue():
                tempValue = tempValue.getNextValue()
                    
            
            tempValue.linkNext(element)

    def getHeadValue(self):
        return self.headValue

    def reverse(self):
        #a -> b -> c -> d
        #d -> c -> b ->  a
        evalElement = self.headValue
        savedPrev = None
        savedNext = None
        saveCurr = None
        while evalElement.getNextValue():
            if evalElement == self.headValue:
                tempElement = evalElement.getNextValue()
                evalElement.linkNext(None)
                savedPrev = evalElement
                evalElement = tempElement
                
            else:
                tempElement = evalElement.getNextValue()
                evalElement.linkNext(savedPrev)
                savedPrev = evalElement
                evalElement = tempElement

        self.headValue = evalElement
        self.headValue.linkNext(savedPrev)

               
                

               
