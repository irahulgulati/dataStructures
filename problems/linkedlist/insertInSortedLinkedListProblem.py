import os
import sys
sys.path.append(".")
from linkedlist.singlylinkedlist.node import Node
from linkedlist import LinkedList

class CustomLinkedList:
    def __init__(
        self,
        numberOfNodes: int
    ) -> None:
        if isinstance(numberOfNodes, int):
            self.singlyLList: LinkedList = LinkedList()
            for _ in range(numberOfNodes):
                self.singlyLList.addNode(_)

    def insert(self, data: int) -> None:
        continueLoop: bool = True
        currentHead: Node = self.singlyLList.head

        if currentHead.data > data:
            oldHead: Node = self.singlyLList.head
            newHead: Node = Node(data)
            self.singlyLList.head = newHead
            self.singlyLList.head.next = oldHead
            return

        while continueLoop:
            if currentHead.data <= data:
                if currentHead.next == None or currentHead.next.data >= data:
                    self.singlyLList.insertAfterNode(currentHead, data)
                    continueLoop = False
                    return

            currentHead = currentHead.next
        

if __name__ == "__main__":
    requiredNumberOfNodes: int = 10
    customLinkedList: CustomLinkedList = CustomLinkedList(
        requiredNumberOfNodes
    )
    customLinkedList.insert(-1)
    customLinkedList.insert(20)
    customLinkedList.insert(12)
    customLinkedList.insert(11)
    customLinkedList.insert(10)
    customLinkedList.insert(-2)
    customLinkedList.insert(19)
    print(customLinkedList.singlyLList.head.data)
    print(customLinkedList.singlyLList.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data)
