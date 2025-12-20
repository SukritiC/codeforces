class Solution:
    def heapify_down(self, arr, ind):
        largest = ind
        lchild = 2*ind+1
        rchild = 2*ind+2

        if lchild < len(arr) and arr[largest] < arr[lchild]:
            largest = lchild
        if rchild < len(arr) and arr[largest] < arr[rchild]:
            largest = rchild
        if largest != ind:
            arr[ind], arr[largest] = arr[largest], arr[ind]
            self.heapify_down(arr, largest)

    def heapify_up(self, nums, ind):
        parent = (ind-1)//2
        if ind > 0:
            if nums[ind] > nums[parent]:
                nums[ind], nums[parent] = nums[parent], nums[ind]
                self.heapify_up(nums, parent)


    def heapify(self, nums, ind, val):
        if nums[ind] < val:
            nums[ind] = val
            self.heapify_up(nums, ind)
        else:
            nums[ind] = val
            self.heapify_down(nums, ind)
