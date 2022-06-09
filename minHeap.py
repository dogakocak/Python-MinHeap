class MinHeap:
    __MAX_SIZE = 100
    __size = 0
    __items = [None] * __MAX_SIZE

    def __Parent(self, n):
        return int((n - 1) / 2)

    def __LeftChild(self, n):
        return int(2 * n + 1)

    def __RightChild(self, n):
        return int(2 * n + 2)

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size >= self.__MAX_SIZE

    def insert(self, itm):
        if not self.isFull():
            self.__items[self.__size] = itm
            self.heapUp(self.__size)
            self.__size += 1

    def deleteMin(self):
        min = 0
        if not self.isEmpty():
            min = self.__items[0]
            self.__items[0] = self.__items[self.__size-1]
            self.heapDown(0)
            self.__size-=1
        return min

    def heapDown(self,loc):
            while loc < self.__size -1:
                if (self.__LeftChild(loc) <= self.__size -1) and (self.__RightChild(loc) <= self.__size -1): # if there is left and right childs
                    if self.__items[self.__LeftChild(loc)] < self.__items[self.__RightChild(loc)]: # if left child is greater than right child
                        if self.__items[loc] < self.__items[self.__LeftChild(loc)]:
                            break
                        tmp = self.__items[loc]
                        self.__items[loc] = self.__items[self.__LeftChild(loc)]
                        self.__items[self.__LeftChild(loc)] = tmp
                        loc = self.__LeftChild(loc)
                    else:
                        if self.__items[loc] < self.__items[self.__RightChild(loc)]:
                            break
                        tmp = self.__items[loc]
                        self.__items[loc] = self.__items[self.__RightChild(loc)]
                        self.__items[self.__RightChild(loc)] = tmp
                        loc = self.__RightChild(loc)
                elif self.__LeftChild(loc) <= self.__size-1: # if there is only left child and there is no condition that there is only the right child because of heap structure
                    if self.__items[loc] < self.__items[self.__LeftChild(loc)]:
                        break
                    tmp = self.__items[loc]
                    self.__items[loc] = self.__items[self.__LeftChild(loc)]
                    self.__items[self.__LeftChild(loc)] = tmp
                    loc = self.__LeftChild(loc)
                else:
                    break





    def heapUp(self, loc):
        while loc > 0:
            if self.__items[loc] < self.__items[self.__Parent(loc)]:
                temp = self.__items[loc]
                self.__items[loc] = self.__items[self.__Parent(loc)]
                self.__items[self.__Parent(loc)] = temp
                loc = self.__Parent(loc)  # updating loc
            else:
                break

    def __preorder(self, loc):
        if loc < self.__size:
            print(self.__items[loc], end=',')
            self.__preorder(self.__LeftChild(loc))
            self.__preorder(self.__RightChild(loc))

    def preorder(self):
        self.__preorder(0)

    def __postOrder(self, loc):
        if loc < self.__size:
            self.__postOrder(self.__LeftChild(loc))
            self.__postOrder(self.__RightChild(loc))
            print(self.__items[loc], end=',')

    def postOrder(self):
        self.__postOrder(0)

    def __inOrder(self, loc):
        if loc < self.__size:
            self.__inOrder(self.__LeftChild(loc))
            print(self.__items[loc], end=',')
            self.__inOrder(self.__RightChild(loc))

    def inOrder(self):
        self.__inOrder(0)


minHeap = MinHeap()
minHeap.insert(3)
minHeap.insert(6)
minHeap.insert(8)
minHeap.insert(12)
minHeap.insert(15)
minHeap.deleteMin()
minHeap.deleteMin()
minHeap.preorder()

