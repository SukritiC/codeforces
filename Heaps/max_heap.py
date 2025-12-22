class Solution:
    def __init__(self):
        self.arr = []  # list to store the max-heap
        self.count = 0  # to store the count of elements in max-heap

    # Function to recursively heapify the array upwards
    def heapifyUp(self, ind):
        parentInd = (ind - 1) // 2

        # If current index holds larger value than the parent
        if ind > 0 and self.arr[ind] > self.arr[parentInd]:
            # Swap the values at the two indices
            self.arr[ind], self.arr[parentInd] = self.arr[parentInd], self.arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(parentInd)
        return

    # Function to recursively heapify the array downwards
    def heapifyDown(self, ind):
        n = len(self.arr)  # Size of the array

        # To store the index of largest element
        largestInd = ind

        # Indices of the left and right children
        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2

        # If the left child holds larger value, update the largest index
        if leftChildInd < n and self.arr[leftChildInd] > self.arr[largestInd]:
            largestInd = leftChildInd

        # If the right child holds larger value, update the largest index
        if rightChildInd < n and self.arr[rightChildInd] > self.arr[largestInd]:
            largestInd = rightChildInd

        # If the largest element index is updated
        if largestInd != ind:
            # Swap the largest element with the current index
            self.arr[largestInd], self.arr[ind] = self.arr[ind], self.arr[largestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(largestInd)
        return

    # Method to intialize the max-heap data structure
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    # Method to insert a given value in the max-heap
    def insert(self, key):
        # Insert the value at the back of the list
        self.arr.append(key)

        # Heapify upwards
        self.heapifyUp(self.count)
        self.count += 1  # Increment the counter
        return

    # Method to change the value at a given index in max-heap
    def changeKey(self, index, new_val):
        # If the current value is replaced with a larger value
        if self.arr[index] < new_val:
            self.arr[index] = new_val
            self.heapifyUp(index)
        # Otherwise (if the current value is replaced with smaller value)
        else:
            self.arr[index] = new_val
            self.heapifyDown(index)
        return

    # Method to extract the maximum value from the max-heap
    def extractMax(self):
        ele = self.arr[0]  # maximum value in the heap

        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]

        # Pop the maximum value from the list
        self.arr.pop()
        self.count -= 1  # Decrement the counter

        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(0)

    # Method to return if the max-heap is empty
    def isEmpty(self):
        return (self.count == 0)

    # Method to return the maximum value in the max-heap
    def getMax(self):
        # Return the value stored at the root
        return self.arr[0]

    # Method to return the size of max-heap
    def heapSize(self):
        return self.count


# Driver code
def main():
    # Creating an object of the Solution class
    heap = Solution()

    # Initializing a max heap data structure
    heap.initializeHeap()

    # Performing different operations
    heap.insert(4);
    print("Inserting 4 in the max-heap")
    heap.insert(1);
    print("Inserting 1 in the max-heap")
    heap.insert(10);
    print("Inserting 10 in the max-heap")
    print("Maximum value in the heap is:", heap.getMax())
    print("Size of max-heap is:", heap.heapSize())
    print("Is heap empty:", heap.isEmpty())
    print("Extracting maximum value from the heap")
    heap.extractMax()
    print("Changing value at index 0 to 16")
    heap.changeKey(0, 16)
    print("Maximum value in the heap is:", heap.getMax())


if __name__ == "__main__":
    main()
