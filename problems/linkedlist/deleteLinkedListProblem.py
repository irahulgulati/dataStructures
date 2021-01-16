import os
import sys
sys.path.append(".")
from linkedlist.singlylinkedlist.node import Node
from linkedlist import LinkedList


def createSinglyLinkedListWithNodes(
    numberOfNodes: int
) -> LinkedList:
    singlyLList: LinkedList = LinkedList()
    for _ in range(numberOfNodes):
        singlyLList.addNode(_)
    return singlyLList


def deleteSinglyLinkedList(
    selectedSinglyLinkedList: LinkedList
) -> bool:
    while selectedSinglyLinkedList.head != None:
        selectedSinglyLinkedList.deleteHead()

    return True if selectedSinglyLinkedList.head is None else False


if __name__ == "__main__":
    requiredNumberOfNodes: int = 10
    singlyLList: LinkedList = createSinglyLinkedListWithNodes(
        requiredNumberOfNodes)
    isDeleted: bool = deleteSinglyLinkedList(singlyLList)
    if isDeleted:
        print("Singly Linkedlist has been deleted")
    else:
        print("There was a problem in deleting selected singly Linkedlist")
