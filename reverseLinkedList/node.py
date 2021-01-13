class Node:
    def __init__(self, value):
        self.value = value
        self.nextValue = None

    def linkNext(self, value):
        self.nextValue = value

    def getNextValue(self):
        return self.nextValue



