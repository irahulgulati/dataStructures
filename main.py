if __name__ == "__main__":
    from linkedlist import DoublyLinkedList
    from linkedlist import LinkedList
    dd: DoublyLinkedList = DoublyLinkedList()
    dd.addNode(20)
    dd.addNode(30)
    dd.addNode(40)
    dd.addHead(15)
    dd.insertAfterNode(dd.head.next, 25)
    dd.deleteHead()
    print(dd.head.data)
