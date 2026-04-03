class LLNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    
    def remove(self, node: LLNode):
        prev = node.prev
        n = node.next
        if node == self.head:
            self.head = n
        if node == self.tail:
            self.tail = prev

        if prev:
            prev.next = n
        if n:
            n.prev = prev

        node.next= None
        node.prev = None
    
    def removeLRU(self):
        # remove current head (LRU)
        if not self.head:
            return
        node = self.head
        self.remove(node) 

    def addMRU(self, node: LLNode):
        # always add to the tail (MRU)
        node.next = None
        if not self.tail:           # empty list
            self.head = node
            self.tail = node
            node.prev = None
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def __init__(self, capacity: int):
        #LRU
        self.head = None
        #MRU
        self.tail = None
        #int :node that keeps the int as the key
        self.intToNode = {}
        self.cap = capacity

        

    def get(self, key: int) -> int:
        if key not in self.intToNode:
            return -1
        node = self.intToNode[key]
        ret = node.val
        if node != self.tail:
            self.remove(node)
            self.addMRU(node)
        return ret

        

    def put(self, key: int, value: int) -> None:
        if key in self.intToNode:
            #update Node and and shift to tail
            node= self.intToNode[key]
            node.val = value
            if node != self.tail:
                self.remove(node)
                self.addMRU(node)

        else:
            #check for capacity
            if len(self.intToNode) == self.cap:
                #evict
                del self.intToNode[self.head.key]
                self.removeLRU()
            
            node = LLNode(key, value)
            self.intToNode[key] = node
            self.addMRU(node)



        
