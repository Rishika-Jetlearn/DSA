from tkinter import*
window=Tk()
window.geometry("430x500")
window.title("Celsius to Farenheit")
window.config(background="#C2EBF5")

#user input
type=Entry(window)
type.grid(row=1,column=1)

#LABELS
lab=Label(window,text="Node value: ",font=("comicsans",16,"bold"))
lab.grid(row=1,column=0)

tree=Label(window)
tree.grid(row=5,column=0)

#Buttons
create=Button(window,text="Create node",bg="lightgreen",fg="black")
create.grid(row=4,column=2,padx=50,pady=30)

insert=Button(window,text="insert node",bg="lightgreen",fg="black")
insert.grid(row=3,column=2,padx=50,pady=30)

search=Button(window,text="search node",bg="lightgreen",fg="black")
search.grid(row=2,column=2,padx=50,pady=30)

exit=Button(window,text="Exit",command=exit,bg="lightgreen",fg="black")
exit.grid(row=2,column=1,padx=50,pady=30)

inorder=Button(window,text="Inorder",bg="lightgreen",fg="black")
inorder.grid(row=2,column=0,padx=50,pady=50)

preorder=Button(window,text="Preorder",bg="lightgreen",fg="black")
preorder.grid(row=3,column=0,padx=50,pady=30)

postorder=Button(window,text="Postorder",bg="lightgreen",fg="black")
postorder.grid(row=4,column=0,padx=50,pady=30)

#run code
window.mainloop()