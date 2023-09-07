class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.value = 0


class DoubleLinkedList:
    _length = 0

    head = Node()
    tail = Node()

    head.next = tail
    tail.prev = head
    #length
    #front,back
    #insert
    #delete
    #get
    def length(self) -> int:
        return self._length
        

    def get(self,index):

        if index < 0 or index > self.length():
            print("인덱스의 값이 유효하지 않습니다.")
            return
            
        i = 0
        ret = self.head
        while i <= index:
            ret = ret.next
            i+=1
            
        return ret

    def get_front(self) -> Node:
        return self.head.next


    def get_back(self) -> Node:
        return self.tail.prev


    def insert(self,index,value) -> Node:
        indexNode = self.get(index)

        if indexNode == None:
            return
        
        newnode = Node()
        newnode.value = value

        self._length += 1

        if self.head.next is self.tail:
            self.head.next = newnode
            self.tail.prev = newnode
            return newnode
        
        if indexNode.prev == None:
            newnode.next = self.head.next
            newnode.next.prev = newnode
            self.head.next = newnode
            return newnode
        
        newnode.next = indexNode.next
        newnode.prev = indexNode
        indexNode.next = newnode
        indexNode.next.prev = newnode
        return newnode

    def insert_front(self,value) -> Node:
        self._length += 1
        return
    

    def insert_back(self,value):
        newnode = Node()
        newnode.value = value

        if self.head.next is self.tail:
            self.head.prev = newnode
            self.tail.next = newnode

            self._length += 1
            return newnode

        newnode.next = self.tail.prev
        newnode.next.next = newnode
        self.tail.prev = newnode

        self._length += 1
        return newnode
        

    def delete(self,index):
        self._length -= 1
        return


    def delete_front(self):
        self._length -= 1
        return
    

    def delete_back(self):
        self._length -= 1
        return
    
dlist = DoubleLinkedList()

dlist.insert(1,1)
dlist.insert(0,1)
dlist.insert(1,3) 
dlist.insert_back(4)


print(dlist.head.next.value)
print(dlist.head.next.next.value)
print(dlist.head.next.next.next.value)