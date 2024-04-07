from tkinter import *
#  pro is varible  to class
pro=Tk()
#  geometry هي ابعاد البرنامج 
pro.geometry('1370x768')
# title عنوان البرنامج
pro.title('Photoshop')
# icon  للبرنامج
#pro.iconbitmap('')
# التحكم ف الابعاد الشاشه ف  الحجم الاصغر و الاكبر ف برنامج
pro.maxsize(1370,768)
pro.minsize(685,384)
# frame 
frame1=Frame(width='1370',height='120',bg='red')
frame1.place(x=1,y=1)
frame2=Frame(width='120',height='768',bg='grey')
frame2.place(x=0,y=120)
# menu اللي ف اعلي شاشه
bar=Menu(pro)
pro.config(menu=bar)
# File in menubar
filemenu=Menu(bar,tearoff=0)
bar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open ')
filemenu.add_command(label='Save ')
filemenu.add_command(label='Save AS ')
filemenu.add_separator()
filemenu.add_command(label='Print')
filemenu.add_command(label='Close')
#000000000000000000000000000000000
# Eidt in menubar
editmenu=Menu(bar,tearoff=0)
bar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')

#0000000000000000000000000000000000000000000000
#imgae in menubar
imagemenu=Menu(bar,tearoff=0)
bar.add_cascade(label='Image', menu=imagemenu)
imagemenu.add_command(label='Resize')
imagemenu.add_command(label='Rotate')
imagemenu.add_command(label='Flip')
imagemenu.add_command(label='Brightness and Contrast')
imagemenu.add_separator()
imagemenu.add_command(label='Colors')
imagemenu.add_command(label='Effects')
#0000000000000000000000000000000000000000000000000000000

# tool in menubar
toolmenu=Menu(bar,tearoff=0)
bar.add_cascade(label='TOOls', menu=toolmenu)
toolmenu.add_command(label='Brush')
toolmenu.add_command(label='Pencil')
toolmenu.add_command(label='Line')
toolmenu.add_command(label='Shape')
toolmenu.add_command(label='Text')

#00000000000000000000000000000000000000000000000
# view in menubar
viewmenu=Menu(bar,tearoff=0)
bar.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Zoom In')
viewmenu.add_command(label='Zoom Out')
viewmenu.add_command(label='Zoom to Fit')



pro.mainloop()
