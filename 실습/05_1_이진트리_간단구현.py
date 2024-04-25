##함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
##변수

##메인 
node1 = TreeNode()
node1.data = 'Jennie'

node2 = TreeNode()
node2.data = 'Jisoo'
node1.left = node2 

node3 = TreeNode()
node3.data = 'Rose'
node1.right = node3

node4 = TreeNode()
node4.data = 'Lisa'
node2.left = node4

node5 = TreeNode()
node5.data = 'Yejin'
node2.right = node5

node6 = TreeNode()
node6.data = 'Ahyeon'
node3.left = node6

root = node1 
print(root.data)
print(root.left.data, root.right.data)
print(root.left.left.data, root.left.right.data, root.right.left.data)





