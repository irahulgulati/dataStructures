from .node import Node


class DoublyLinkedList:
    """
    * Creating LinkedList class which represent the linkedlist
    * data structure. Each object instantiate of this class
    * will give the individual instance of linkedlist with
    * access to linkedlist operational methods.
    * `head` is class attribute which is of type Node and denotes
    * the first node of the instantiated linkedlist
    * `tail` is class attribute which is of type Node and denotes
    * the last node of the instantiated linkedlist
    """
    head: Node = None
    tail: Node = None

    def addNode(self, data):
        if not data:
            return
        if self.head is None:
            newNode: Node = Node(data)
            self.head = newNode
            self.tail = newNode
            return

        currentNode: Node = self.head
        while currentNode.next is not None:
            currentNode: Node = currentNode.next

        newNode: Node = Node(data, prev=currentNode)
        currentNode.next = newNode
        self.tail: Node = newNode

    def deleteWithValue(self, data: int):
        if self.head is None:
            return

        currentNode: Node = self.head
        nextNode: Node = self.head.next
        tailNode: Node = self.tail

        if currentNode.data == data:
            self.deleteHead()
            return

        if tailNode.data == data:
            self.tail = tailNode.prev
            return

        while nextNode is not None and nextNode.data != data:
            currentNode: Node = nextNode
            nextNode: Node = nextNode.next

        if nextNode == None:
            return
        else:
            currentNode.next = nextNode.next
            if nextNode.next is not None:
                nextNode.next.prev = currentNode

    def searchWithValue(self, data: int):
        if self.head == None:
            return

        currentNode: Node = self.head
        while currentNode.data != data:
            currentNode = currentNode.next
            if currentNode is None:
                return

        return currentNode

    def insertAfterNode(self, selectedNode: Node, data: int):
        if self.head == None:
            return

        currentNode: Node = self.head
        nextNode: Node = self.head.next

        if nextNode is None:
            if currentNode == selectedNode:
                self.addNode(data)
            else:
                return
        else:
            while currentNode != selectedNode:
                currentNode = nextNode
                nextNode = nextNode.next

            newNode: Node = Node(data, prev=currentNode, next=currentNode.next)
            currentNode.next = newNode
            nextNode.prev = newNode

    def addHead(self, data: int):
        if self.head == None:
            self.addNode(data)

        else:
            oldHead: Node = self.head
            newHead: Node = Node(data, next=oldHead)
            oldHead.prev = newHead
            self.head = newHead

    def deleteTail(self):
        if self.tail == None:
            return

        oldTail: Node = self.tail
        newTail: Node = oldTail.prev
        newTail.next = None
        self.tail = newTail
        return self.tail

    def deleteHead(self):
        if self.head is None:
            return

        self.head = self.head.next
