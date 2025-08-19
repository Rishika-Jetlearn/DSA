from tkinter import*
import treeDS
import copy
window=Tk()
window.geometry("430x500")
window.title("BST")
window.config(background="#C2EBF5")
root=None

def create_node():
    value=Value_of_node.get()
    global root
    root=treeDS.tree_node(value)
    #"tree.config(text=f"{value}")"

def insert_node(start,value):
    if start is None:
        print(root.key)
        return treeDS.tree_node(value)
    elif start.key>value:
        print("left",root.key)
        start.left_ch=insert_node(start.left_ch,value)
        
    else:
        print("right",root.key)
        start.right_ch=insert_node(start.right_ch,value)
        
    #"tree.config(text=f"{value}")"
    
def inorder_tvrs(start):
    print(start.key)
    if start.left_ch is not None:
        inorder_tvrs(start.left_ch)

    result=tree.cget("text") + "-" + str(start.key)
    print(result)
    tree.config(text=f"{result}")

    if start.right_ch is not None:
        inorder_tvrs(start.right_ch)

"""def insert_node(value):
    global root
    if root is None:
        create_node()
    else:
        current=root
        while True:
            if value<current.key:
                if current.left_ch is None:
                    =current.left_ch"""


#user input
Value_of_node=Entry(window)
Value_of_node.grid(row=1,column=1)

start_lable=Label(window,text="Start: ")
start_lable.grid(row=1,column=0)

#LABELS
lab=Label(window,text="Node value: ",font=("comicsans",16,"bold"))
lab.grid(row=1,column=0)

tree=Label(window,)
tree.grid(row=5,column=0)

#Buttons
create=Button(window,text="Create node",bg="lightgreen",fg="black",command=create_node)
create.grid(row=4,column=2,padx=50,pady=30)

insert=Button(window,text="insert node",bg="lightgreen",fg="black",command=lambda:insert_node(root,Value_of_node.get()))
insert.grid(row=3,column=2,padx=50,pady=30)

search=Button(window,text="search node",bg="lightgreen",fg="black")
search.grid(row=2,column=2,padx=50,pady=30)

exit=Button(window,text="Exit",command=exit,bg="lightgreen",fg="black")
exit.grid(row=2,column=1,padx=50,pady=30)

inorder=Button(window,text="Inorder",bg="lightgreen",fg="black",command=lambda: inorder_tvrs(root))
inorder.grid(row=2,column=0,padx=50,pady=50)

preorder=Button(window,text="Preorder",bg="lightgreen",fg="black")
preorder.grid(row=3,column=0,padx=50,pady=30)

postorder=Button(window,text="Postorder",bg="lightgreen",fg="black")
postorder.grid(row=4,column=0,padx=50,pady=30)


window.mainloop()