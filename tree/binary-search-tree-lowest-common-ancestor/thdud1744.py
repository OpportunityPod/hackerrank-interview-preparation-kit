class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def search(node, v):
    while True:
        if not node:
            return None
        compare = v - node.info
        if compare ==0:
            return node
        if compare <0:
            node = node.left
        if compare >0:
            node = node.right

def lca(node, v1,v2):
    if node.info == v1 or node.info == v2:
        return node
    if search(node.left,v1) and search(node.left,v2):
        return lca(node.left,v1,v2)
    if search(node.right,v1) and search(node.right,v2):
        return lca(node.right,v1,v2)
    else:
        return node

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
