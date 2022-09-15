
import functools
import os, sys
from tkinter import *
from time import sleep
def CreateFivemScriptFunc():
    firstname_info = firstname.get()
    pathfolder_info = pathfolder.get()
    pathfile_info = pathfile.get()
    # print(firstname_info,lastname_info,age_info)
    pathhfolder = pathfolder_info
    pathsss = pathfile_info
    os.chdir(pathhfolder)
    NewFolder=firstname_info
    os.makedirs(NewFolder)
    sleep(3)
    os.chdir(pathsss)
    fp = open('client'+'.lua', 'w')
    fp.write('--write client natives here')
    fp.close()
    fp2 = open('server'+'.lua', 'w')
    fp2.write('--write server natives here')
    fp2.close()
    fp3 = open('config'+'.lua', 'w')
    fp3.write('Config                            = {}')
    fp3.close()
    fp4 = open('fxmanifest'+'.lua', 'w')
    str='"adamant"'
    str2='"gta5"'
    str3='"write script name here"'
    str4='"discription here"'
    str5='"KonarPlus#6627"'
    str6='"1.0.0"'
    str7='"config.lua"'
    str8='"client.lua"'
    str9='"server.lua"'
    fp4.write('fx_version'+ ' '+str+'')
    fp4.write('\n')
    fp4.write('game'+ ' '+str2+'')
    fp4.write('\n')
    fp4.write('name'+ ' '+str3+'')
    fp4.write('\n')
    fp4.write('description'+ ' '+str4+'')
    fp4.write('\n')
    fp4.write('author'+ ' '+str5+'')
    fp4.write('\n')
    fp4.write('version'+ ' '+str6+'')
    fp4.write('\n')
    fp4.write('\n')
    fp4.write('shared_script'+ ' '+str7+'')
    fp4.write('\n')
    fp4.write('client_scripts'+ ' '+str8+'')
    fp4.write('\n')
    fp4.write('server_scripts'+ ' '+str9+'')
    fp4.close()

app = Tk()
app.geometry("500x500")
app.title("Create Your First Script Fivem")
firstname_text = Label(text="Script Name :")
pathfolder_text = Label(text="Put The Path Folder Here :")
pathfile_text = Label(text="Path File Here/Script Name :")
firstname_text.place(x=15,y=70)
pathfolder_text.place(x=15,y=125)
pathfile_text.place(x=15,y=175)
firstname = StringVar()
pathfolder = StringVar()
pathfile = StringVar()
first_name_entry = Entry(textvariable=firstname,width="30")
pathfolder_entry = Entry(textvariable=pathfolder,width="30")
pathfile_entry = Entry(textvariable=pathfile,width="30")
first_name_entry.place(x=15,y=100)
pathfolder_entry.place(x=15,y=150)
pathfile_entry.place(x=15,y=200)
button = Button(app,text="Create",command=CreateFivemScriptFunc,width="30",height="2",bg="grey")
button.place(x=15,y=290)
mainloop()

