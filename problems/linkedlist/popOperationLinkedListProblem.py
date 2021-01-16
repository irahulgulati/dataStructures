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

    def pop(
        self
    ) -> int:
        if self.singlyLList is None:
            return
        if self.singlyLList.head is None:
            return
        poppedNodeData: Node = self.singlyLList.head.data
        self.singlyLList.head = self.singlyLList.head.next
        return poppedNodeData


if __name__ == "__main__":
    requiredNumberOfNodes: int = 10
    customLinkedList: CustomLinkedList = CustomLinkedList(
        requiredNumberOfNodes)
    poppedHeadData1: int = customLinkedList.pop()
    poppedHeadData2: int = customLinkedList.pop()
    print(poppedHeadData1, poppedHeadData2)
    print(customLinkedList.singlyLList.head.data)
