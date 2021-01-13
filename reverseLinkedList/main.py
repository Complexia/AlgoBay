from linked_list import LinkedList

l1 = LinkedList()
l1.insert(5)
l1.insert(8)
l1.insert(9)
l1.insert(17)
l1.insert(4)

l1.reverse()

print(l1.getHeadValue().getNextValue().getNextValue().value)
