class tree_node():
    def __init__(self,key):
        self.key=key
        self.left_ch=None
        self.right_ch=None

def inorder(start):
    if start.left_ch is not None:
        inorder(start.left_ch)

    print(start.key)

    if start.right_ch is not None:
        inorder(start.right_ch)

def preorder(start):
    print(start.key)

    if start.left_ch is not None:
        preorder(start.left_ch)

    if start.right_ch is not None:
        preorder(start.right_ch)

def postorder(start):
    if start.left_ch is not None:
        postorder(start.left_ch)

    if start.right_ch is not None:
        postorder(start.right_ch)
    
    print(start.key)


"""root=tree_node("A")
root.left_ch=tree_node("B")
root.right_ch=tree_node("C")

root.left_ch.left_ch=tree_node("D")
root.left_ch.right_ch=tree_node("E")

root.right_ch.left_ch=tree_node("F")
root.right_ch.right_ch=tree_node("G")

inorder(root)
print("***********************")
preorder(root)
print("***********************")
postorder(root)"""