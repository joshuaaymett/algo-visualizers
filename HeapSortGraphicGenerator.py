# Joshua Aymett
# CISP 430, Professor Dan Ross

from graphviz import Digraph
import math
import sys

imageIndex = 0

def printArray(arr, n):
    i = 0
    print('[', end = '')
    while(i < n):
        if(i != 0):
            print(', ', end = '')
        print( arr[i], end = '' )
        i += 1
    print(']')

def swap(arr, parent, child, n):
    global imageIndex
    if(imageIndex > 45):
        sys.exit(1)

    # Duplicate list
    nums = []
    nums.extend(arr)

    # Index of the parent value
    parentIndex = nums.index(parent)
    childIndex = nums.index(child)

    # Swap positions of parent and child
    nums[parentIndex] = child
    nums[childIndex] = parent

    g = Digraph('G', format='png', filename='cluster.gv' + str(imageIndex))
    lbl = "Swapping " + str(child) + " and " + str(parent)
    g.attr(label=lbl, color='blue')
    g.attr('node', color='blue')
    imageIndex += 1


    # Create and open image
    parentIndexDraw = None
    i=1
    while(i <= n):
            layer = int(math.log(i+1, 2))
            # Child's offset from left of tree
            childOffsetFromLeft = i - (pow(2, layer) -1)
            parentOffsetFromLeft = int(childOffsetFromLeft / 2)
            parentIndexDraw = int(pow(2, layer - 1) + parentOffsetFromLeft) - 1
            if(nums[i] == parent):
                g.edge(str(nums[parentIndexDraw]), str(nums[i]), color='red', dir="back")
            else:
                g.edge(str(nums[parentIndexDraw]), str(nums[i]), color='purple')
            i += 1
    g.view()
    printArray(nums,n)
    
    # Check if another switch is necessary

    difference = int((parentIndex/2)) + 1
    # If parent's parent is greater than parent (new child), swap
    if (parentIndex != 0 and nums[int(parentIndex - difference) ] > nums[int(parentIndex)]):
        swap(nums, nums[parentIndex - difference ], nums[parentIndex], n )
    elif (n < len(nums) - 1):
        draw(nums, n+1)
    else: 
        return

def draw(nums, n):
    global imageIndex
    if(imageIndex > 45):
        sys.exit(1)

    # Create file
    g = Digraph('G', format='png', filename='cluster.gv' + str(imageIndex))
    lbl = "Inserting " + str(nums[n])
    g.attr(label=lbl, color='purple')
    g.attr('node', color='blue')
    imageIndex += 1

    # Index of parent node
    parentIndex = None

    if(n==0):
        g.node(str(nums[n]))
    else:
        i=1
        while(i <= n):
            layer = int(math.log(i+1, 2))
            # Child's offset from left of tree
            childOffsetFromLeft = i - (pow(2, layer) -1)
            parentOffsetFromLeft = int(childOffsetFromLeft / 2)
            parentIndex = int(pow(2, layer - 1) + parentOffsetFromLeft) - 1
            if(nums[i] == nums[n]):
                g.edge(str(nums[parentIndex]), str(nums[i]), color='green')
            else:
                g.edge(str(nums[parentIndex]), str(nums[i]), color='purple')
            i += 1
    g.view()
    printArray(nums,n)

    if(n != 0 and nums[int(parentIndex)] > nums[n]): # if parent greater than child, swap
        swap(nums, nums[parentIndex], nums[n], n)
    elif (n < len(nums) - 1):
        draw(nums, n+1)
    else: 
        return

array = [90, 60, 30, 35, 40, 45, 85, 55,50,75,80,70,25,20,65,10]

draw(array, 0)