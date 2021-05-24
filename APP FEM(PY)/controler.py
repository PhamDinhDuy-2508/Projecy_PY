from tkinter import * 
import Newin 
import pandas as pd 
import app 
import solved 
import check
class Menubar(Menu,Newin._create) : 
    def __init__(self , master , controller) : 
        Menu.__init__(self ,controller) 
        self.s = []  
        s =  self.s
        self.controller = controller 
        menubar = Menu(self , tearoff = 0 )  
        menubar = Menu(self, tearoff=0) 
        self.add_cascade(label="File", underline=0, menu=menubar)
        menubar.add_command(label="Material Choice", underline=1 , command = self._MaterialPage) 
        menubar.add_command(label = "All Component" , underline = 2 , command = self.InformationPage)
        menubar.add_separator()
        menubar.add_command(label="Exit", underline=2, command=self.onexit) 
        self.key = []
    def onexit(self):
        quit()      
    def get(self,s)   : 
            return s 
    def _MaterialPage(self) :  
        lst = ' '
        s = [] 
        Newin._create.materialPage(self, lst )   
    def check(self,str1) : 
        s= str1
        #s = Newin._create.informationPage(self,s)  
        print(s)
        return s 
    def InformationPage(self) :    
        newindow= Toplevel(self)  
        k = check.MainApp.check(self) 
        re =solved.Ketqua(k)
        newindow.label = Label(newindow,text  = f"TOTAL STIFF : {re['ts']}") 
        newindow.label.pack()


          




        