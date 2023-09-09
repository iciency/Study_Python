from list import AbstractList


class Stack:
    def __init__(self, type: AbstractList) -> None:
        self._list = type

    def push(self, value):
        self._list.insert_back(value)
        return

    def pop(self):
        if self._list.length() <= 0:
            raise Exception("더이상 pop()을 할 수 없습니다.")

        stack = self._list.get_back()
        self._list.delete_back()

        return stack

    def size(self):
        return self._list.length()
