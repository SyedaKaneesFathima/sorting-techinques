def findPivotIndex(nums, left, right):
    # storing the pivot here 
    pivot = nums[right]
   
    for index in range(left, right):
        if nums[index] < pivot:
            temp = nums[position]
            nums[position] = nums[index]
            nums[index] = temp 
            position += 1 
 
    temp = nums[right]
    nums[right] = nums[position]
    nums[position] = temp 
    return position
 
def performQuickSort(nums, left, right)
    if left >= right:
        return 
    pivotIndex = findPivotIndex(nums, left, right)
    print(nums)
 
    performQuickSort(nums, left, pivotIndex - 1)
    performQuickSort(nums, pivotIndex + 1, right)
n=int(input()) 
nums=list(map(int,input().split())
n = len(nums)
print("Before sorting", nums)
 
performQuickSort(nums, 0, n - 1)
print(nums)
 
