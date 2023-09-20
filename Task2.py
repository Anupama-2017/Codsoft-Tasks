import tkinter as tk
def clear_entries():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result.set("")
def calculate(operation):
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == "+":
        result.set(f"Result: {num1 + num2:.2f}")
    elif operation == "-":
        result.set(f"Result: {num1 - num2:.2f}")
    elif operation == "*":
        result.set(f"Result: {num1 * num2:.2f}")
    elif operation == "/":
        if num2 == 0:
            result.set("Error: Division by zero")
        else:
            result.set(f"Result: {num1 / num2:.2f}")
root = tk.Tk()
root.title("Simple Calc")
root.geometry("400x200")
root.configure(bg="lightgrey")
label_num1 = tk.Label(root, text="Enter num1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()
label_num2 = tk.Label(root, text="Enter num2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()
operation_frame = tk.Frame(root,bg="lightgrey")
operation_frame.pack()
label_res = tk.Label(root, text="result")
label_res.pack()
add_button = tk.Button(operation_frame, text="+", command=lambda: calculate("+"))
subtract_button = tk.Button(operation_frame, text="-", command=lambda: calculate("-"))
multiply_button = tk.Button(operation_frame, text="*", command=lambda: calculate("*"))
divide_button = tk.Button(operation_frame, text="/", command=lambda: calculate("/"))
subtract_button.pack(side="left",padx=5,pady=5)
add_button.pack(side="left",padx=5,pady=5)
multiply_button.pack(side="left",padx=5,pady=5)
divide_button.pack(side="left",padx=5,pady=5)
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14),bg="grey")
result_label.pack()
clear_button = tk.Button(root,text="Clear",command=clear_entries)
clear_button.pack()
root.mainloop()
