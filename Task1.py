import tkinter
root=tkinter.Tk()
root.configure(bg="lightgrey")
root.title('To-Do List Box')
tasks=[]
def add_task():
    task=txt_input.get()
    if task!='':
        tasks.append(task)
        update_list()
        display['text']="task added"
    else:
        display['text']="enter a task"
    txt_input.delete(0,'end')
def update_list():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)
def delete():
    task=lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    update_list()
    display['text']="deleted"
def delete_all():
    global tasks
    tasks=[]
    update_list()
def number_of_task():
    number_of_task=len(tasks)
    msg="total tasks: %s" %number_of_task
    display['text']=msg
def clear_listbox():
    lb_tasks.delete(0,"end")
title=tkinter.Label(root,text="To_do list",bg='lightgrey')
title.grid(row=0,column=1)
add_task_msg=tkinter.Label(root,text="enter the task name",bg=None)
add_task_msg.grid(row=2,column=0)
display=tkinter.Label(root,text="",bg='grey')
display.grid(row=1,column=1)
txt_input=tkinter.Entry(root,width=15)
txt_input.grid(row=2,column=1)
btn_add_task=tkinter.Button(root,text="Add Task",fg="black",bg=None,command=add_task)
btn_add_task.grid(row=8,column=0)
btn_delete=tkinter.Button(root,text="Delete",fg="black",bg=None,command=delete)
btn_delete.grid(row=9,column=0)
btn_number_of_task=tkinter.Button(root,text="Number of Tasks",fg="black",bg=None,command=number_of_task)
btn_number_of_task.grid(row=8,column=1)
btn_delete_all=tkinter.Button(root,text="Delete all",fg="black",bg=None,command=delete_all)
btn_delete_all.grid(row=8,column=3)
lb_tasks=tkinter.Listbox(root)
lb_tasks.grid(row=3,column=1,rowspan=3)
root.mainloop()
