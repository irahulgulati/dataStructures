class Node:
    """
    * Creating the class Node whose one/single instantiated
    * object represents as one node of doubly linkedlist
    * For visual representation of this class please check
    * below.
     |!!!!!!!!!!!!!!!!!!!!!!!!!!|
    |    data    | prev | next |
   |!!!!!!!!!!!!!!!!!!!!!!!!!!|

    * class attribute `next` denotes the next pointer of the node
    * class attribute `data` denotes the data of the node and for 
    * this use case is limited to integer data type
    * class attribute `prev` denotes the previous pointer of the node
    """
    prev = None
    next = None
    data: int = None

    def __init__(self, data: int, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
