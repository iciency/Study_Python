# from stack import Stack
# from linkedList import LinkedList

# ComCount = int(input())

# if 1 <= ComCount <= 100000:
#     Stack1 = Stack(LinkedList())
#     for i in range(ComCount):

#         num_list = list(map(int, input().split()))

#         if not len(num_list) == 2:
#             X = num_list[0]
#         else:
#             Stack1.push(num_list[1])
#             print("push",num_list[1])
#             X = num_list[0]
            
#         if X == 2:
#             if Stack1.size() <= 0:
#                 print("p", -1)
#             else:
#                 print("pop",Stack1.pop())

#         elif X == 3:
#             print("p",Stack1.size() +1)

#         elif X == 4:
#             if Stack1.size() <= 0:
#                 print("p",1)
#             else:
#                 print("p",0)
#         elif X == 5:
#             if not Stack1.size() <= 0:
#                 value = Stack1.pop()
#                 print("p",value)
#                 Stack1.push(value)
#             else:
#                 print("p",-1)


# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,x):
#         self.stack.append(x)

#     def pop(self):
#         return self.stack.pop() if self.stack else -1

#     def size(self):
#         return len(self.stack)
    
# ComCount = int(input())

# if 1 <= ComCount <= 100000:
#     Stack1 = Stack()
#     for i in range(ComCount):

#         num_list = list(map(int, input().split()))

#         if not len(num_list) == 2:
#             X = num_list[0]
#         else:
#             Stack1.push(num_list[1])
#             X = num_list[0]
            
#         if X == 2:
#             if Stack1.size() <= 0:
#                 print(-1)
#             else:
#                 print(Stack1.pop())

#         elif X == 3:
#             print(Stack1.size())

#         elif X == 4:
#             if Stack1.size() <= 0:
#                 print(1)
#             else:
#                 print(0)
#         elif X == 5:
#             if not Stack1.size() <= 0:
#                 value = Stack1.pop()
#                 print(value)
#                 Stack1.push(value)
#             else:
#                 print(-1)

import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    command = sys.stdin.readline()

    #1
    if command[0] == "1":
        stack.append(int(command[2]))

    #2    
    elif command[0] == "2":
        if stack == []:
            print(-1) 
        else:
            print(stack.pop())

    #3
    elif command[0] == "3":
        print(len(stack))
    
    #4
    elif command[0] == "4":
        if stack == []:
            print(1)
        else:
            print(0)

    elif command[0] == "5":
        if stack == []:
            print(-1)
        else:
            value = stack.pop()
            print(value)
            stack.append(value)