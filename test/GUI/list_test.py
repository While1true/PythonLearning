#encoding:utf_8
from Tix import *
from tkMessageBox import showinfo
class ListDir:
    TITLE='文件夹查看器'
    def __init__(self):
        self.__build_ui()
        self._ListPath(None)
        print('>>> init finish')
        mainloop()

    def __build_ui(self):
        self.__build_window()

        self.__build_component()

    def __build_window(self):
        window = self.window = Tk()
        self.sv=StringVar(window)
        window.geometry('400x500')
        window.resizable(0, 0)
        window.title(self.TITLE)
        window.iconbitmap('file.ico')
        self.frame=Frame(window,bg="lightgreen")
        print('>>> window created')
    def __build_component(self):
        print('---> start creat component')
        '''addAuthor Label'''
        label=Label(self.window,text='welcome to my python App Author: 不听话的好孩子'.title(),fg='green').pack(side=BOTTOM)
        self.__build_entry()
        frame=self.frame

        '''add path label'''
        self.pathLabel=Label(frame,text="当前路径: ",justify='center',fg="white",bg="#ff4070",anchor=W)
        self.pathLabel.pack(expand=False,fill=X)

        '''add path list'''
        scrollbar=Scrollbar(frame)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.list=Listbox(frame,height=15,width=50,yscrollcommand=scrollbar.set)
        self.list.bind('<Double-1>',self.__doubleClickFolder)
        scrollbar.config(command=self.list.yview)
        self.list.pack(side=LEFT,fill=Y)
        frame.pack(expand=YES,fill=BOTH)


    '''双击了item'''
    def __doubleClickFolder(self,event):
        self.checkindex=self.list.curselection()
        self.currentPath=self.list.get(self.checkindex)
        if not self.currentPath:
            return
        self.currentPath=self.sv.get() + "\\" + self.currentPath
        if(os.path.isdir(self.currentPath)):
            self._ListPath(self.currentPath)
        else:
            if('.txt' in self.currentPath):
                os.system('notepad '+self.currentPath)
            elif(os.access(self.currentPath,os.R_OK)):
                os.system(self.currentPath)

            else:
                showinfo("选择了文件如下文件",os.path.abspath(self.currentPath))
        # print('<<< user clicked'+' selected content '+self.currentPath)

    '''获取entry内容'''
    def __getEntryText(self, event):
        self.currentPath = self.sv.get()
        self._ListPath(self.currentPath)
        print('<<< user clicked',self.sv.get(),type(event))

    def _ListPath(self,path):
        if not path:
            path=sys.path[0]
        self.__list(path)


    def __list(self,path):
        if(os.path.isdir(path)):
            os.chdir(path)
            self.pathLabel.config(text="当前路径："+path)
            self.sv.set(os.path.abspath(path))
            self.input.update()

            os_listdir = os.listdir(path)
            listview=self.list
            listview.delete(0,END)
            listview.insert(END, os.pardir)
            for file in os_listdir:
                listview.insert(END,file)
            listview.selection_set(0)


            print(path)
        elif os.path.isfile(path) and os.path.pardir(path):
            self._ListPath(os.path.pardir(path))
        else:
            self.sv.set(path+' is no a directoy')
            print(self.sv.get())
        self.window.update()


    def __build_entry(self):
        bf=Frame(self.window)
        self.input=Entry(bf,width=40,justify='center',textvariable=self.sv,foreground ="#ff4070",background ='gray')
        self.input.bind('<Return>',self.__getEntryText)
        self.input.grid(row=0,column=0,sticky=E)
        self.listbutton=Button(bf,text='查看',padx=10,background ='lightblue',command=lambda :self.__getEntryText(None))
        self.listbutton.grid(row=0,column=1,sticky=E+W)
        bf.pack(fill=X,side=BOTTOM)
        self.input.focus_force()


if __name__ == '__main__':
    ListDir()

