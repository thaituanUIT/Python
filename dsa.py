
import math
import time
import random
import copy
import sys

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def print(self):
        print(self.data)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

root.print()
root.left.print()
root.right.print()
root.left.left.print()
root.left.right.print()
