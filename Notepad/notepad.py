import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, scrolledtext
from datetime import datetime

def new_file():
    global file_path
    if len(text_widget.get('1.0', tk.END+'-1c')) > 0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            save_file()
        else:
            text_widget.delete(1.0, tk.END)
    root.title("Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(1.0, file.read())
        root.title(f"Notepad - {file_path}")

def save_file():
    global file_path
    if not file_path:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get(1.0, tk.END))
        root.title(f"Notepad - {file_path}")

def save_file_as():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get(1.0, tk.END))
        root.title(f"Notepad - {file_path}")

def exit_app():
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

def cut_text():
    text_widget.event_generate("<<Cut>>")

def copy_text():
    text_widget.event_generate("<<Copy>>")

def paste_text():
    text_widget.event_generate("<<Paste>>")

def find_text():
    text_to_find = simpledialog.askstring("Find", "Find what:")
    if text_to_find:
        start_pos = text_widget.search(text_to_find, "1.0", tk.END)
        while start_pos:
            end_pos = f"{start_pos}+{len(text_to_find)}c"
            text_widget.tag_add("found", start_pos, end_pos)
            start_pos = text_widget.search(text_to_find, end_pos, tk.END)
        text_widget.tag_configure("found", background="yellow")

def select_all_text():
    text_widget.tag_add("sel", "1.0", tk.END)

def insert_time_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    text_widget.insert(tk.INSERT, dt_string)

def about_notepad():
    messagebox.showinfo("About Notepad", "Notepad by kajal")

root = tk.Tk()
root.title('Notepad')
root.geometry('800x600')

file_path = ''

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_app)

edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Find', command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all_text)
edit_menu.add_command(label='Insert Time/Date', command=insert_time_date)

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About Notepad', command=about_notepad)

text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
text_widget.pack(fill=tk.BOTH, expand=True)

root.mainloop()
