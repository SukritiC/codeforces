class Solution:
    def heapifyDown(self, arr, ind):
        n = len(arr)  # Size of the array

        # Index of smallest element
        smallest_Ind = ind

        # Indices of the left and right children
        leftChild_Ind = 2 * ind + 1
        rightChild_Ind = 2 * ind + 2

        # If the left child holds smaller value, update the smallest index
        if leftChild_Ind < n and arr[leftChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = leftChild_Ind

        # If the right child holds smaller value, update the smallest index
        if rightChild_Ind < n and arr[rightChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = rightChild_Ind

        # If the smallest element index is updated
        if smallest_Ind != ind:
            # Swap the smallest element with the current index
            arr[smallest_Ind], arr[ind] = arr[ind], arr[smallest_Ind]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, smallest_Ind)

        return

    # Function to convert given array into a min-heap
    def buildMinHeap(self, nums):
        n = len(nums)

        # Iterate backwards on the non-leaf nodes
        for i in range(n // 2 - 1, -1, -1):
            # Heapify each node downwards
            self.heapifyDown(nums, i)