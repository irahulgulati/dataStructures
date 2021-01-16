from .node import Node


class LinkedList:
    """
    * Creating LinkedList class which represent the linkedlist
    * data structure. Each object instantiate of this class
    * will give the individual instance of linkedlist with
    * access to linkedlist operational methods.
    * `head` is class attribute which is of type Node and denotes
    * the head node of the instantiated linkedlist
    """
    head: Node = None

    # addNode method to add signle node to linkedlist
    def addNode(
        self,
        data: int
    ) -> None:
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            currentNode = self.head

            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def deleteWithValue(
        self,
        data: int
    ) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        currentNode = self.head
        if currentNode.next.data == data:
            currentNode.next = currentNode.next.next

        currentNode = currentNode.next

    def searchWithValue(
        self,
        data: int
    ) -> Node:
        if self.head.data == data:
            return self.head

        currentNode: Node = self.head
        while currentNode.data != data:
            currentNode = currentNode.next
        return currentNode

    def size(
        self
    ) -> int:
        size: int = 0

        if self.head is None:
            return 0

        currentNode: Node = self.head     
        while currentNode:
            size += 1
            currentNode = currentNode.next

        return size

    def insertAfterNode(
        self,
        prevNode: Node,
        data: int
    ) -> None:
        if self.size() == 0:
            return

        currentNode: Node = self.head
        while currentNode != prevNode:
            currentNode = currentNode.next

        newNode: Node = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode

    def deleteAfterNode(
        self,
        prevNode: Node
    ) -> None:
        if self.size() == 0:
            return

        currentNode: Node = self.head
        while currentNode != prevNode:
            currentNode = currentNode.next

        if currentNode.next == None:
            return

        currentNode.next = currentNode.next.next

    def deleteHead(
        self
    ) -> None:
        if self.head is None:
            return
        self.head = self.head.next
        return

    def insertHead(
        self,
        data: int
    ) -> None:
        if self.head is None:
            self.addNode(data)
            return
        oldHead: Node = self.head
        self.head = Node(data)
        self.head.next = oldHead
        return
