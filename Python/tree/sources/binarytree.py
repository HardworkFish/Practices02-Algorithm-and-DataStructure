#!/usr/bin/env python
# Python 实现二叉树

#创建根节点
class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# 插入节点
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# 打印二叉树
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()