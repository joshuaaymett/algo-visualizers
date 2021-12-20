
# Joshua Aymett, Linear Hash
# CISP 430, Professor Dan Ross

from graphviz import Digraph
import math
import sys

imageIndex = 0

def draw(nums):
    global imageIndex
    hashArr = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    g = Digraph('G', format='png', filename='cluster.gv' + str(imageIndex), node_attr={'color': 'black', 'shape': 'record', 'fontcolor': 'black', 'height': '.1', 'width' : '.3'})
    i = 0
    while(i < len(nums)):
        g.node('array')
        g.attr(label='0        1        2        3        4        5        6        7        8        9', fontcolor='purple')
        if(hashArr[nums[i] % 10] == '_'):
            hashArr[nums[i] % 10] = str(nums[i])
        else:
            j = 1
            while(hashArr[((nums[i] % 10) + j) % 10] != '_'):
                j += 1
                if(j >= 10):
                    print("Error, array full")
                    sys.exit()
            hashArr[((nums[i] % 10) + j) % 10] = str(nums[i])
            g.edge( f'array:<f{str(nums[i] % 10)}>', f'array:f{str(((nums[i] % 10) + j) % 10)}',color='purple')
        g.node('array', f'<f0>  {hashArr[0]} |<f1> {hashArr[1]} |<f2> {hashArr[2]} |<f3> {hashArr[3]} |<f4> {hashArr[4]} |<f5> {hashArr[5]} |<f6> {hashArr[6]} |<f7> {hashArr[7]} |<f8> {hashArr[8]} |<f9> {hashArr[9]} ',  width='5')
        g.view()
        imageIndex  += 1
        i += 1
        g.filename = 'cluster.gv' + str(imageIndex)


nums = [22, 3, 12, 1, 18, 36, 33, 9]

draw(nums)