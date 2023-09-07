from typing import Optional
from typing import cast
from typing import Tuple
import json
from list import AbstractList

class Node:
    def __init__(self):
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
        self.value: int = 0

class LinkedList(AbstractList):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
   
    def _get_node(self, index: int) -> Node:
        if self.length() == 0: 
            raise Exception('head is None Type')
        if self.head.next is None:
            raise Exception('head is None Type')

        retNode: Node = self.head.next
        for _ in range(index):
            if retNode.next == self.tail : raise IndexError('Index out of range')
            if retNode.next is not None:
                retNode = retNode.next
            else:
                raise Exception('invalid node state')
        return retNode
    # node앞에 insert한다.
    def _insert(self, node: Node, value: int) -> bool:
        insert_node = Node()
        insert_node.value = value

        if node.prev is None:
            raise Exception('Invalid Type')
        prev_node: Node = node.prev
        next_node: Node = node        

        prev_node.next = insert_node
        insert_node.prev = prev_node
        next_node.prev = insert_node
        insert_node.next = next_node
        
        self.size = self.size + 1
        return True

    def _delete(self, del_node: Node) -> None:
        if del_node.prev is None:
            raise Exception('_delete del_node.prev is None')
        if del_node.next is None:
            raise Exception('_delete del_node.next is None')
        prev_node: Node = del_node.prev
        next_node: Node = del_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        del_node.prev = None
        del_node.next = None
        del del_node
        self.size = self.size - 1
    
    
    def get(self, index: int) -> int:
        return self._get_node(index).value    
    def get_front(self) -> int:
        return self.get(0)
    def get_back(self) -> int:
        if self.length() == 0: raise Exception('tail is None Type')

        if self.tail.prev is None:
            raise Exception('tail is None Type')
        retNode: Node = self.tail.prev
        return retNode.value
    
    

    # 해당인덱스에 추가하는 함수. 리스트가 비워있으면 working하지않는다.
    def insert_index(self, index: int, value: int) -> None:
        select_node = self._get_node(index)
        self._insert(select_node, value)
    # 제일 앞에 추가한다.
    def insert_front(self, value) -> None: 
        if self.head.next is None:
            raise Exception('insert_front Invalid Type')
        head_next_node: Node = self.head.next
        self._insert(head_next_node, value)
    # 제일 뒤에 추가한다.
    def insert_back(self, value) -> None:
        tail_prev_node: Node = self.tail
        self._insert(tail_prev_node, value)

    # 해당인덱스의 노드를 제거한다.
    def delete(self, index: int) -> None:
        target_node = self._get_node(index)
        self._delete(target_node)

    # 제일 앞의 노드를 제거한다.
    def delete_front(self):
        if self.length() == 0: raise Exception('tail is None Type')

        self.delete(0)
    # 제일 뒤의 노드를 제거한다.
    def delete_back(self):
        if self.length() == 0: raise Exception('tail is None Type')
        if self.tail.prev == None: raise Exception('self.tail.prev is None Type')
        target_node: Node = self.tail.prev
        self._delete(target_node)
    
    def length(self) -> int:
        return self.size
    
    def print(self) -> None:
        if self.head.next == None: raise Exception('self.head.next is None Type')
        iter: Node = self.head.next
        json_result = []
        while iter != self.tail:
            json_result.append(iter.value)
            if iter.next == None: raise Exception('iter.next is None Type')
            iter = iter.next
        print(json.dumps(json_result))
        print('array length', self.length())

        if self.length() != 0:
            print('front', self.get_front(), self.get_back())
        print()