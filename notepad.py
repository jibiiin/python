from tkinter import*
from tkinter import filedialog as fd
import tkinter.font as tkfont
from tkinter import colorchooser as cc
window=Tk()
def new():
    text.delete("1.0","end")
    window.title("notepad")
def file_open():
    file=fd.askopenfile(parent=window,mode="rb",title="open a file")
    if file:
        content=file.read()
        text.delete("1.0","end")
        text.insert("1.0",content)
        file()
        window.title(file.name)
def file_save():
    file=fd.asksaveasfile(parent=window,mode="w",defaultextension=".txt",filetypes=[("document file","*.text"),("all file","*.*")])
    if file:
        content=text.get("1.o","end")
        file.write(content) 
        file.close()
        window.title(file.name)
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")
def bold():
    text.config(font=tkfont.Font(weight=tkfont.BOLD))
def italic():
    text.config(font=tkfont.Font(slant=tkfont.ITALIC))
def under():
    text.config(font=tkfont.Font(underline=True))
def bcolor():
    color=cc.askcolor(title="select a color")
    text.config(bg=color[1])
def fcolor():
    color=cc.askcolor(title="select a color")
    text.config(fg=color[1])



text=Text(wrap="word")
text.pack(side="top",fill="both",expand="True")
menubar=Menu()
window.config(menu=menubar)



file_menu=Menu(menubar)
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new",command=new)
file_menu.add_command(label="open",command=file_open)
file_menu.add_command(label="save",command=file_save)
file_menu.add_command(label="exit",command=quit)
edit_menu=Menu(menubar)
menubar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy)
edit_menu.add_command(label="paste",command=paste)
txt_menu=Menu(menubar)
menubar.add_cascade(label="txt",menu=txt_menu)
txt_menu.add_command(label="bold",command=bold)
txt_menu.add_command(label="italic",command=italic)
txt_menu.add_command(label="underline",command=under)

color_menu=Menu(txt_menu)
txt_menu.add_cascade(label="color",menu=color_menu)
color_menu.add_command(label="background color",command=bcolor)
color_menu.add_command(label="forground color",command=fcolor)
font_menu=Menu(txt_menu)
txt_menu.add_cascade(label="font",menu=font_menu)
font_menu.add_command(label="font size increase",command="")
font_menu.add_command(label="font size decrease",command="")
font_menu.add_command(label="font style",command="")






window.mainloop()

