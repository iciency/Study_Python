from abc import *

class AbstractList(metaclass=ABCMeta):
    @abstractmethod
    def get(self, index: int) -> int:
        pass
    
    @abstractmethod
    def get_front(self) -> int:
        pass

    @abstractmethod
    def get_back(self) -> int:
        pass

    # 해당인덱스에 추가하는 함수. 리스트가 비워있으면 working하지않는다.
    @abstractmethod
    def insert_index(self, index: int, value: int) -> None:
        pass
    # 제일 앞에 추가한다.
    @abstractmethod
    def insert_front(self, value) -> None: 
        pass
    # 제일 뒤에 추가한다.
    @abstractmethod
    def insert_back(self, value) -> None:
        pass

    # 해당인덱스의 노드를 제거한다.
    @abstractmethod
    def delete(self, index: int) -> None:
        pass

    # 제일 앞의 노드를 제거한다.
    @abstractmethod
    def delete_front(self):
        pass
        
    # 제일 뒤의 노드를 제거한다.
    @abstractmethod
    def delete_back(self):
        pass
    
    @abstractmethod
    def length(self) -> int:
        pass
    
    @abstractmethod
    def print(self) -> None:
        pass