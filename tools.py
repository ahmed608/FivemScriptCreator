from tkinter import *
from tkinter import messagebox
from pygments import lex
from pygments.lexers import LuaLexer
from pygments.styles import get_style_by_name
from helpers import convert_code, load_replacements, load_replacements_test, load_replacements_test2


def open_tools_page(parent_window, is_dark_theme, freamework):
    def go_back():
        tools_window.destroy()
        parent_window.deiconify()

    def copy_converted_code():
        tools_window.clipboard_clear()
        tools_window.clipboard_append(converted_text.get("1.0", END).strip())
        messagebox.showinfo("Success", "Converted code copied to clipboard!")

    def update_line_numbers(event=None):
        line_numbers_text.config(state=NORMAL)
        line_numbers_text.delete("1.0", END)
        row, col = code_text.index(END).split('.')
        for i in range(1, int(row)):
            line_numbers_text.insert(END, f'{i}\n')
        line_numbers_text.config(state=DISABLED)

    def on_scroll(*args):
        code_text.yview(*args)
        line_numbers_text.yview(*args)

    def on_text_scroll(event):
        code_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        line_numbers_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        update_line_numbers()

    parent_window.withdraw()
    tools_window = Toplevel()
    tools_window.title("Convert Framework")
    tools_window.iconbitmap("images\\egypt_studio_logo.ico")
    tools_window.geometry("1500x600")
    tools_window.resizable(False, False)

    bg_color = 'black' if is_dark_theme else 'white'
    fg_color = 'white' if is_dark_theme else 'black'
    tools_window.configure(bg=bg_color)

    code_font = ("Courier New", 12, "normal")

    Label(tools_window, text="Enter your code:", bg=bg_color, fg=fg_color).pack(pady=10)

    code_frame = Frame(tools_window)
    code_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    line_numbers_text = Text(code_frame, width=4, bg=bg_color, fg=fg_color, font=code_font, state=DISABLED)
    line_numbers_text.pack(side=LEFT, fill=Y)

    scroll_bar = Scrollbar(code_frame)
    scroll_bar.pack(side=RIGHT, fill=Y)

    code_text = Text(code_frame, height=10, bg=bg_color, fg=fg_color, insertbackground=fg_color, font=code_font, undo=True, yscrollcommand=scroll_bar.set)
    code_text.pack(side=LEFT, fill=BOTH, expand=True)
    scroll_bar.config(command=on_scroll)

    code_text.bind('<KeyRelease>', update_line_numbers)
    code_text.bind('<MouseWheel>', on_text_scroll)
    code_text.bind('<Button-1>', update_line_numbers)
    
    converted_frame = Frame(tools_window)
    converted_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

    converted_scroll_bar = Scrollbar(converted_frame)
    converted_scroll_bar.pack(side=RIGHT, fill=Y)

    converted_text = Text(converted_frame, height=10, width=40, state=NORMAL, bg=bg_color, fg=fg_color, insertbackground=fg_color, font=code_font, yscrollcommand=converted_scroll_bar.set)
    converted_text.pack(fill=BOTH, expand=True)
    converted_scroll_bar.config(command=converted_text.yview)
    converted_text.config(state=DISABLED)

    def convert():
        if freamework == "esx":
            original_code = code_text.get("1.0", END).strip()  
            replacements = load_replacements()
            converted_code = convert_code(original_code, replacements)
            converted_text.config(state=NORMAL)
            converted_text.delete("1.0", END)
            converted_text.insert("1.0", converted_code)
            converted_text.config(state=DISABLED)
        elif freamework == "vRP":
            original_code = code_text.get("1.0", END).strip()  
            replacements_Test = load_replacements_test()
            converted_code = convert_code(original_code, replacements_Test)
            converted_text.config(state=NORMAL)
            converted_text.delete("1.0", END)
            converted_text.insert("1.0", converted_code)
            converted_text.config(state=DISABLED)
        elif freamework == "vRP_Qb":
            original_code = code_text.get("1.0", END).strip()  
            replacements_Test2 = load_replacements_test2()
            converted_code = convert_code(original_code, replacements_Test2)
            converted_text.config(state=NORMAL)
            converted_text.delete("1.0", END)
            converted_text.insert("1.0", converted_code)
            converted_text.config(state=DISABLED)
        

    def copy(event=None):
        try:
            tools_window.clipboard_clear()
            text = code_text.get(SEL_FIRST, SEL_LAST).strip()
            tools_window.clipboard_append(text)
        except TclError:
            pass

    def paste():
        try:
            clipboard_text = tools_window.clipboard_get().strip()
            code_text.insert(INSERT, clipboard_text)
        except TclError:
            pass



    convert_button = Button(tools_window, text="Convert", command=convert, bg=bg_color, fg=fg_color)
    convert_button.pack(pady=20)

    copy_converted_code_button = Button(tools_window, text="Copy Converted Code", command=copy_converted_code, bg=bg_color, fg=fg_color)
    copy_converted_code_button.pack(pady=10)

    back_button = Button(tools_window, text="Back to Main Page", command=go_back, bg=bg_color, fg=fg_color)
    back_button.pack()

    update_line_numbers()