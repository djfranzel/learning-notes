
# these are notes for my python course on linked lists
# https://www.udemy.com/course/python-linked-list/learn/lecture/8122100#overview

# why have a linked list? 
# with normal list, inserting an item at the beginning will cause every subsequent item's index to be updated
# linked lists carry their location in relation to other items, not as an index
# there are 4 types
# 1. singly linked list
# 2. doubly linked list
# 3. circular linked list
# 4. circular doubly linked list

# singly - contains a reference to the next item in the list
# doubly - contains references to the next and previous items in the list
# circular - contains reference to the next item and the last item contains reference to the first
# circular double - contains reference to previous, next and last item has reference to first, and first item has reference to last

# singly - two data points in the node, data such as a string, and the reference to the next item
# the memory address is the value in 'next', they are stored separately and accessed based on next or previous
# del will delete the address, but must properly handle previous node structure to update its 'next'

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp

    def isListEmpty(self):
        return self.head is None

    def listLength(self):
        count = 0
        currentNode = self.head
        while not currentNode.next is None:
            count += 1
            currentNode = currentNode.next
        return count
    
    def deleteEnd(self):
        if not self.isListEmpty():
            if self.head.next is None:
                self.deleteHead()
                return
            currentNode = self.head
            while currentNode.next is not None:
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = None
            del currentNode
        else:
            print('List is empty')

    def deleteHead(self):
        if not self.isListEmpty():
            previousHead = self.head    
            self.head = self.head.next
            previousHead.next = None
            del previousHead
        else:
            print('List is empty')

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print('Invalid position!')
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1 

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while not lastNode.next is None:
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print('list is empty')
            return
        currentNode = self.head
        while not currentNode is None:
            print(currentNode.data)
            currentNode = currentNode.next

linkedList = LinkedList()
linkedList.insertEnd(Node(10))
linkedList.insertEnd(Node(20))
linkedList.insertAt(Node(15), 1)
linkedList.deleteHead()
linkedList.printList()

