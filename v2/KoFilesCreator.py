
from cProfile import label
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
    str='"cerulean"'
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

def CreateFivemScriptFuncEsx():
    firstname_info = firstname.get()
    pathfolder_info = pathfolder.get()
    pathfile_info = pathfile.get()
    # print(firstname_info,lastname_info,age_info)
    pathhfolder = pathfolder_info
    pathsss = pathfile_info
    os.chdir(pathhfolder)
    NewFolder = firstname_info
    os.makedirs(NewFolder)
    sleep(3)
    os.chdir(pathsss)
    fp = open('client' + '.lua', 'w')
    fp.write('ESX = exports["es_extended"]:getSharedObject()')
    fp.close()
    fp2 = open('server' + '.lua', 'w')
    fp2.write('ESX = exports["es_extended"]:getSharedObject()')
    fp2.close()
    fp3 = open('config' + '.lua', 'w')
    fp3.write('Config                            = {}')
    fp3.close()
    fp4 = open('fxmanifest' + '.lua', 'w')
    str = '"cerulean"'
    str2 = '"gta5"'
    str3 = '"write script name here"'
    str4 = '"discription here"'
    str5 = '"KonarPlus#6627"'
    str6 = '"1.0.0"'
    str7 = '"config.lua"'
    str8 = '"client.lua"'
    str9 = '"server.lua"'
    fp4.write('fx_version' + ' ' + str + '')
    fp4.write('\n')
    fp4.write('game' + ' ' + str2 + '')
    fp4.write('\n')
    fp4.write('name' + ' ' + str3 + '')
    fp4.write('\n')
    fp4.write('description' + ' ' + str4 + '')
    fp4.write('\n')
    fp4.write('author' + ' ' + str5 + '')
    fp4.write('\n')
    fp4.write('version' + ' ' + str6 + '')
    fp4.write('\n')
    fp4.write('\n')
    fp4.write('shared_script' + ' ' + str7 + '')
    fp4.write('\n')
    fp4.write('client_scripts' + ' ' + str8 + '')
    fp4.write('\n')
    fp4.write('server_scripts' + ' ' + str9 + '')
    fp4.close()
def CreateFivemScriptFuncQb():
    firstname_info = firstname.get()
    pathfolder_info = pathfolder.get()
    pathfile_info = pathfile.get()
    # print(firstname_info,lastname_info,age_info)
    pathhfolder = pathfolder_info
    pathsss = pathfile_info
    os.chdir(pathhfolder)
    NewFolder = firstname_info
    os.makedirs(NewFolder)
    sleep(3)
    os.chdir(pathsss)
    fp = open('client' + '.lua', 'w')
    fp.write('local QBCore = exports["qb-core"]:GetCoreObject()')
    fp.close()
    fp2 = open('server' + '.lua', 'w')
    fp2.write('local QBCore = exports["qb-core"]:GetCoreObject()')
    fp2.close()
    fp3 = open('config' + '.lua', 'w')
    fp3.write('Config                            = {}')
    fp3.close()
    fp4 = open('fxmanifest' + '.lua', 'w')
    str = '"cerulean"'
    str2 = '"gta5"'
    str3 = '"write script name here"'
    str4 = '"discription here"'
    str5 = '"KonarPlus#6627"'
    str6 = '"1.0.0"'
    str7 = '"config.lua"'
    str8 = '"client.lua"'
    str9 = '"server.lua"'
    fp4.write('fx_version' + ' ' + str + '')
    fp4.write('\n')
    fp4.write('game' + ' ' + str2 + '')
    fp4.write('\n')
    fp4.write('name' + ' ' + str3 + '')
    fp4.write('\n')
    fp4.write('description' + ' ' + str4 + '')
    fp4.write('\n')
    fp4.write('author' + ' ' + str5 + '')
    fp4.write('\n')
    fp4.write('version' + ' ' + str6 + '')
    fp4.write('\n')
    fp4.write('\n')
    fp4.write('shared_script' + ' ' + str7 + '')
    fp4.write('\n')
    fp4.write('client_scripts' + ' ' + str8 + '')
    fp4.write('\n')
    fp4.write('server_scripts' + ' ' + str9 + '')
    fp4.close()

window = Tk()
window.geometry("300x400")
window.title("Create Your First Script Fivem")
window.iconbitmap("images\\egypt_studio_logo.ico")
imagebackground = PhotoImage(file = "images\\konarplus.png")
label1 = Label(window, image=imagebackground)
label1.pack()
photo = PhotoImage(file = "images\\qb-core.png")
firstname_text = Label(text="Script Name :")
pathfolder_text = Label(text="Put The Path Folder Here :")
pathfile_text = Label(text="Path File Here/Script Name :")
firstname_text.place(x=15,y=20)
pathfolder_text.place(x=15,y=80)
pathfile_text.place(x=15,y=140)
firstname = StringVar()
pathfolder = StringVar()
pathfile = StringVar()
first_name_entry = Entry(textvariable=firstname,width="30")
pathfolder_entry = Entry(textvariable=pathfolder,width="30")
pathfile_entry = Entry(textvariable=pathfile,width="30")
first_name_entry.place(x=15,y=50)
pathfolder_entry.place(x=15,y=110)
pathfile_entry.place(x=15,y=170)
photoimage = photo.subsample(5, 5)
photo1 = PhotoImage(file = "images\\standlone.png")
photoimage1 = photo1.subsample(5, 5)
photo2 = PhotoImage(file = "images\\EsxCore.png")
photoimage2 = photo2.subsample(5, 5)
button = Button(window, text = ' Create Standlone ',command=CreateFivemScriptFunc,image = photoimage1,compound = LEFT)
button.place(x=15,y=220)
buttonesx = Button(window, text = '   Create Esx           ',command=CreateFivemScriptFuncEsx, image = photoimage2,compound = LEFT)
buttonesx.place(x=15,y=340)
buttonqb = Button(window, text = '    Create Qb          ',command=CreateFivemScriptFuncQb, image = photoimage,compound = LEFT)
buttonqb.place(x=15,y=280)
mainloop()
