import os
import sys
sys.path.append(".")
from linkedlist.singlylinkedlist.node import Node
from linkedlist import LinkedList
from typing import List

def createLinkedList(listOfNodes: List[int]) -> LinkedList:
    customLinkedList: LinkedList = LinkedList()
    [ customLinkedList.addNode(nodes) for nodes in listOfNodes ]
    return customLinkedList

def sortLinkedList(
    selectedLinkedList: LinkedList
) -> LinkedList:
    sortedLinkedList: LinkedList = LinkedList()
    
    currentSelectedNode: Node = selectedLinkedList.head 
    while currentSelectedNode is not None:

        keepOnLooping: bool = True
        currentNewListNode: Node = sortedLinkedList.head

        if currentNewListNode is None:
            sortedLinkedList.addNode(currentSelectedNode.data)
        else:

            if currentNewListNode.data >= currentSelectedNode.data:
                sortedLinkedList.insertHead(currentSelectedNode.data)

            else:
                while keepOnLooping:
                    if currentNewListNode.data <= currentSelectedNode.data:
                        if (
                            currentNewListNode.next is None
                            or currentNewListNode.next.data
                            >= currentSelectedNode.data
                        ):
                            sortedLinkedList.insertAfterNode(
                                currentNewListNode,
                                currentSelectedNode.data
                            )
                            keepOnLooping = False
                        else:
                            currentNewListNode = currentNewListNode.next

        currentSelectedNode = currentSelectedNode.next
    return sortedLinkedList

if __name__ == "__main__":
    listOfNodes: list = [20,101,18,34,1,5,-10000000,100000000, 0,]
    ll: LinkedList = createLinkedList(
        listOfNodes=listOfNodes
    )
    sortedLinkedList: LinkedList = sortLinkedList(ll)
    print(sortedLinkedList.head.data)
    print(sortedLinkedList.head.next.data)
    print(sortedLinkedList.head.next.next.data)
    print(sortedLinkedList.head.next.next.next.data)
    print(sortedLinkedList.head.next.next.next.next.data)
    print(sortedLinkedList.head.next.next.next.next.next.data)
    print(sortedLinkedList.head.next.next.next.next.next.next.data)
    print(sortedLinkedList.head.next.next.next.next.next.next.next.data)
    print(sortedLinkedList.head.next.next.next.next.next.next.next.next.data)