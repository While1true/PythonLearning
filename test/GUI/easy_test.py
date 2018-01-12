#encoding:utf_8
from functools import partial
from Tix import Tk,Button,X
from tkMessageBox import showinfo,showwarning,showerror
import win32com.client
from PIL import ImageTk as it,Image
TITLE="Welcome to this world "

WARN="warn"
CRIT="crit"
REGU="regu"
SIGNS={"please be c a r e f u l ":WARN,
       "very d a n g e r o u s ":CRIT,
       "have fun":REGU,
       "help help":WARN,
       "nice job":REGU}

action_warn=lambda :showwarning(WARN,WARN+" pressed")
action_crit=lambda :showerror(CRIT,CRIT+" pressed")
action_regu=lambda :showinfo(REGU,REGU+" pressed")
action_INFO=lambda :showinfo(REGU,"whatever you want,whatever you do,it works!")

top=Tk()
top.iconbitmap('App.ico')

# image = it.PhotoImage(file="GIF2.gif")
Button(top,text='chose one to see what may happened',command=action_INFO
       ,compound='right',bg='green',fg='white',bitmap='info',padx=10,pady=10).pack()

builderButton = partial(Button, top)
WarnButton=partial(builderButton,command=action_warn,bg='green',fg='white')
CritButton=partial(builderButton,command=action_crit,bg='red',fg='white')
ReguButton=partial(builderButton,command=action_regu,bg='grey',fg='white')

for (key,value) in SIGNS.iteritems():
    cmd="{0}Button(text='{1}'{2}).pack(fill=X,expand=True)".format(value.title(),key,
           ".upper()" if value==CRIT else ".title()")
    eval(cmd)
top.mainloop()


