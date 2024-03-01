from tkinter import *
import os
from time import sleep
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
import time

is_dark_theme = True

w = Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)
def new_win():
    def create_lua_file(filename, content):
        with open(filename, 'w') as fp:
            fp.write(content)

    def create_fivem_script(script_type):
        firstname_info = firstname.get().strip()
        if not firstname_info:
            messagebox.showerror("error", "Please Write Script Name")
            return

        if firstname_info == 'write script name here':
            messagebox.showerror("error", "Please Write Script Name")
            return

        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        pathhfolder = os.path.join(folder_path, firstname_info)
        os.makedirs(pathhfolder, exist_ok=True)
        sleep(3)
        os.chdir(pathhfolder)

        client_content = ''
        server_content = ''
        config_content = 'Config = {}\n'

        fxmanifest_content = f'''
        fx_version 'cerulean'
        game 'gta5'
        name 'write script name here'
        description 'discription here'
        author 'KonarPlus#6627'
        version '1.0.0'
        lua54 'yes'
        shared_script 'config.lua'
        client_script 'client.lua'
        server_script 'server.lua'
        '''

        if script_type == 'standalone':
            client_content = '-- write client natives here'
            server_content = '-- write server natives here'
        elif script_type == 'esx':
            client_content = 'ESX = exports["es_extended"]:getSharedObject()'
            server_content = 'ESX = exports["es_extended"]:getSharedObject()'
        elif script_type == 'qb':
            client_content = 'local QBCore = exports["qb-core"]:GetCoreObject()'
            server_content = 'local QBCore = exports["qb-core"]:GetCoreObject()'

        create_lua_file('client.lua', client_content)
        create_lua_file('server.lua', server_content)
        create_lua_file('config.lua', config_content)
        create_lua_file('fxmanifest.lua', fxmanifest_content)

    def toggle_dark_theme():
        global is_dark_theme
        is_dark_theme = not is_dark_theme
        update_theme()

    def update_theme():
        if is_dark_theme:
            window.configure(bg='black')

            button.config(bg='black', fg='white', activebackground='black', image=dark_image)
            top_right_label.config(bg='black', fg='white', text="")

            buttonstanlone.config(bg='black', fg='white', activebackground='black', image=standlone_imagedark)
            buttonesx.config(bg='black', fg='white', activebackground='black', image=esxdark)
            buttonqb.config(bg='black', fg='white', activebackground='black', image=qbdark)
        else:
            window.configure(bg='white')

            button.config(bg='white', activebackground='white', fg='black', image=light_image)
            top_right_label.config(bg='white', fg='black', text="")
            buttonstanlone.config(bg='white', fg='white', activebackground='white', image=standlone_imagelight)
            buttonesx.config(bg='white', fg='white', activebackground='white', image=esxwhite)
            buttonqb.config(bg='white', fg='white', activebackground='white', image=qblight)


    window = Tk()
    window.title("Script Creator")
    window.iconbitmap("images\\egypt_studio_logo.ico")

    window_width = 800
    window_height = 800

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    firstname = StringVar()


    first_name_entry = Entry(window, textvariable=firstname, width=40, font=('Arial', 12), fg='grey')
    first_name_entry.place(x=250, y=220)


    first_name_entry.insert(0, "write script name here")


    def clear_placeholder(event):
        if first_name_entry.get() == "write script name here":
            first_name_entry.delete(0, "end")
            first_name_entry.config(fg='black')


    def add_placeholder(event):
        if not first_name_entry.get():
            first_name_entry.insert(0, "write script name here")
            first_name_entry.config(fg='grey')


    first_name_entry.bind("<FocusIn>", clear_placeholder)
    first_name_entry.bind("<FocusOut>", add_placeholder)

    standlone_imagelight =  PhotoImage(file="images\\standlonelight.png")
    standlone_imagedark = PhotoImage(file="images\\standlonedark.png")
    qblight = PhotoImage(file="images\\qblight.png")
    qbdark = PhotoImage(file="images\\qbdark.png")
    esxwhite = PhotoImage(file="images\\esxwhite.png")
    esxdark = PhotoImage(file="images\\esxdark.png")
    light_image = PhotoImage(file="images\\light.png")
    dark_image = PhotoImage(file="images\\dark.png")

    buttonstanlone = Button(window, command=lambda: create_fivem_script('standalone'), image=light_image, bd=0, width=214, height=98, highlightthickness=0, takefocus=False, relief=FLAT, overrelief=FLAT)

    buttonstanlone.place(x=300, y=290)

    buttonesx = Button(window, command=lambda: create_fivem_script('esx'), image= light_image, bd=0, width=214, height=98, highlightthickness=0, takefocus=False, relief=FLAT, overrelief=FLAT)

    buttonesx.place(x=300, y=400)
    buttonqb =  Button(window, command=lambda: create_fivem_script('qb'), image=light_image, bd=0, width=214, height=98, highlightthickness=0, takefocus=False, relief=FLAT, overrelief=FLAT)

    buttonqb.place(x=300, y=510)


    toggle_button = Button(window, command=toggle_dark_theme, image=light_image, bd=-5, width=100, height=50, highlightthickness=0, takefocus=False, relief=FLAT, overrelief=FLAT)
    toggle_button.place(relx=1.0, anchor='ne', x=-50, y=50)

    button = Button(window, command=toggle_dark_theme, image=light_image, bd=-5, width=100, height=50,  highlightthickness=0, takefocus=False, relief=FLAT, overrelief=FLAT)
    button.place(relx=1.0, anchor='ne', x=-50, y=50)


    top_right_label = Label(window, text="", bg=window.cget('bg'), fg='white' if is_dark_theme else 'black')
    top_right_label.place(relx=1.0, anchor='ne', x=-10, y=10)


    style = ttk.Style()
    style.configure("Dark.TButton", foreground="white", background="black")
    style.configure("Light.TButton", foreground="black", background="white")


    window.resizable(False, False)
    update_theme()

Frame(w, width=427, height=250, bg='#272727').place(x=0, y=0)
label1 = Label(w, text='Egypt Studios', fg='white', bg='#272727')  # decorate it
label1.configure(font=("Game Of Squids", 24, "bold"))  # You need to install this font in your PC or try another one
label1.place(x=80, y=70)

image_studio = ImageTk.PhotoImage(Image.open('egypt_studio_logo.png'))
label_studio_image = Label(w, background = '#272727', activebackground = '#272727', image=image_studio, border=0)
label_studio_image.place(x=320, y=40)

label2 = Label(w, text='Loading...', fg='white', bg='#272727')  # decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10, y=215)


image_a = ImageTk.PhotoImage(Image.open('c2.png'))
image_b = ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(3):  # 5loops
    l1 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

w.destroy()

new_win()

w.mainloop()


