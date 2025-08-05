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

root=tree_node("A")
root.left_ch=tree_node("B")
root.right_ch=tree_node("C")

root.left_ch.left_ch=tree_node("D")
root.left_ch.right_ch=tree_node("E")

root.right_ch.left_ch=tree_node("F")
root.right_ch.right_ch=tree_node("G")

inorder(root)