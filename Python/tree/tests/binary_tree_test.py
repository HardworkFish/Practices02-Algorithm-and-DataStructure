from Python.tree.sources.binarytree import Node

# 构造树，插入节点
root = Node(4)
root.insert(Node(5))
root.insert(Node(2))
root.insert(Node(3))
root.insert(Node(1))

print('Binary Tree: ', end=" ")
root.print_tree()

print('\nPreorder Traversal :', root.preorder_traversal(root))
print('NoPreorder Traversal :', root.no_preorder_traversal(root))
print('Inorder Traversal: ', root.inorder_traversal(root))
print('NoInorder Traversal: ', root.no_inorder_traversal(root))
print('Postorder Traversal: ', root.postorder_traversal(root))
print('No Postorder Traversal: ', root.no_postorder_traversal(root))
