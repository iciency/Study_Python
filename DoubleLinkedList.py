class Node:
    def __Init__(self):
        prev = None
        next = None
        value = 0

length = 0

head = Node()
tail = Node()

head.next = tail
tail.prev = head

#경우의 수(0 미만의 수를 인덱스로 주었는가?, get의 index가 길이를 넘어 섯는가?,)
class DoubleLinkedList:
    #length

    #front,back
    #insert
    #delete
    #get
    def length(self) -> int:
        global length
        return length
        

    def get(self,index)-> Node:
        return


    def get_front(self) -> Node:
        return 


    def get_back(self) -> Node:
        return 


    def insert(self,index,value) -> Node:
        global length
        length += 1
        return


    def insert_front(self,value) -> Node:
        return
    

    def insert_back(self,value) -> Node:
        return
    

    def delete(self,index):
        return


    def delete_front(self):
        return
    

    def delete_back(self):
        return
    
    