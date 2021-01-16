class Node:
    """
    * Creating the class Node whose one/single instantiated
    * object represents as one node of single linkedlist
    * For visual representation of this class please check
    * below.
     |!!!!!!!!!!!!!!!!!!!!|
    |    data    |  next |
   |!!!!!!!!!!!!!!!!!!!!|

    * class attribute `next` denotes the next pointer of the node
    * class attribute `data` denotes the data of the node and for 
    * this use case is limited to integer data type
    """
    next = None
    data: int = None

    # constructor to make data population of node easy
    def __init__(self, data: int, next=None):
        if not isinstance(data, int):
            return
        self.data: int = data
        self.next = next