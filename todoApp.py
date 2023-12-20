from tkinter import *
from tkinter import messagebox

root = Tk()
root.configure(background='skyblue')
root.geometry('250x300')

todo_list = []
counter = 1


def submit():
    global counter

    content = task.get()+"\n"

    if (content == ""):
        messagebox.showerror("input error")

    todo_list.append(content)
    textArea.insert('end -1 chars', str(counter)+". "+content)
    counter += 1-
    task.delete(0, END)


def delete():
    global counter
    if len(todo_list) == 0:
        messagebox.showerror("No task")
        return

    idx = int(dlt_task.get())
    if (idx == 0 or idx > len(todo_list)):
        messagebox.showerror("No task")
        return
    todo_list.pop(idx-1)
    counter -= 1

    dlt_task.delete(0, END)
    textArea.delete(1.0, END)

    for i in range(len(todo_list)):
        textArea.insert('end -1 chars', str(i+1)+". "+todo_list[i])


titl = Label(root, text="TODO APP", font=(
    'calibari', 25), bg='gray', fg='white').grid(row=0, column=1)

task = Entry(root, width=40)
task.grid(row=1, column=1, padx=20)

btn = Button(root, text="Submit", bg="lightgray", command=submit).grid(
    row=2, column=1)

textArea = Text(root, height=5, width=30, font="lucida 10")
textArea.grid(row=3, column=1, padx=10)

dlt = Button(root, text="Delete", bg="lightgray", command=delete).grid(
    row=4, column=1)

dlt_task = Entry(root, width=40)
dlt_task.grid(row=5, column=1, padx=20)

exit = Button(root, text="Exit", bg="lightgray", command=root.quit).grid(
    row=6, column=1)

root.mainloop()
