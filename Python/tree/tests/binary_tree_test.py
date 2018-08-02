from tree.sources.binarytree import Node

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print('Binary Tree: ',end=" ")
root.PrintTree()

print('\nPreorder Traversal :', root.PreorderTraversal(root))
print('NoPreorder Traversal :', root.NoPreorderTraversal(root))
print('Inorder Traversal: ', root.InorderTraversal(root))
print('NoInorder Traversal: ', root.NoInorderTraversal(root))
print('Postorder Traversal: ', root.PostorderTraversal(root))
print('No Postorder Traversal: ', root.NoPostorderTraversal(root))