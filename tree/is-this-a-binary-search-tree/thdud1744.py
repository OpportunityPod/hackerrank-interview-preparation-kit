def isBST(node, minKey, maxKey):
     if not node:
        return True
     if node.data <= minKey or node.data >= maxKey:
        return False
     return isBST(node.left, minKey, node.data) and isBST(node.right, node.data, maxKey)

def checkBST(root):
    if isBST(root, 0, 10000):
        return True
    else:
        return False