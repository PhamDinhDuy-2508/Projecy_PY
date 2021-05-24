from tkinter import * 
from tkinter import ttk  
from tkinter import messagebox 
import numpy as np   
import sys 
import pandas
import string 
import Algorithms    
import Newin
import controler 
class rootapp(Tk)  : 
    def __init__(self):
        super().__init__()
        self.title("FEM APP")
        self._frame = None
        self.switch_frame(MainApp)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)import csv
from csv import writer 
import numpy as np 
import Algorithms
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        menubar = self._frame.menubar(self)
        self.configure(menu=menubar)
class MainApp(Frame , Newin._create):  
    def __init__(self, master ):
        Frame.__init__(self , master ) 
        super().__init__() 
        global lst 
        self.menuber = controler.Menubar(self,master) 
        Frame.config(self , bg = 'white' , width = 100)
        Frame(self , width = 200 , height = 200)
        self.Label1 = Label(self , text = 'SELECT PROBLEM' , font = ('Times' , 20 , 'bold') , bg = 'LightBlue' , relief = RAISED )  
        self.Label1.grid(row = 0 , column = 1 )  
        self.promblem1 = Button(self , text = 'Problem1 ' ,  font  = ('calibri' , 12 , 'bold') , bg = 'LightBlue2', command = lambda : master.switch_frame(Problem1)  ) 
        self.promblem1.grid(row =1  , column = 1 , padx = 10 , pady = 10 )   
        self.problem2 = Button (self , text = 'Prombem2 ' , font = ('calibri' , 12 , 'bold') , bg = 'LightBlue2') 
        self.problem2.grid(row =  2 , column =  1  ,  padx = 12 , pady = 12 )     
    def menubar(self , option ) : 
        menubar = controler.Menubar(self , option) 
        return menubar   
class Problem1(Frame,Newin._create) : 
    def __init__(self , master)  :  
        Frame.__init__(self) 
        super().__init__()  
        global lst,_pos,Val,_dictval
        
        Frame.config(self , bg = 'white' , width = 100   )    
        self.label1 = Label(self , text = 'input Indices ' , font = ('calibri' , 20 ,'bold') , bg = 'LightBlue3' , relief = RAISED)   
        self.label1.grid(row  =   0 , column = 1  , padx = 10 , pady = 10  )    
        self.LabelEntrycoordinate = Label(self , text = 'number of Point ', font = ('Times' ,  10 , 'italic' ,'bold'),bg = 'old lace' )  
        self.LabelEntrycoordinate.grid(row = 2 , column = 0 , padx = 5 , pady = 5 )
        self.entrycoordinate = Entry(self, width  = 10 , bd = 2 )  
        self.entrycoordinate.grid(row  = 2 , column =  1  , padx = 10 , pady = 5 )  
        self.ok = Button(self,text ='OK' , font =('Times' , 9 , 'italic' , 'bold') , bg = 'old lace' ,width = 10 , command  = self._check )   
        self.back = Button(self,text =  '<-----' , font =('Times' , 9 , 'italic' , 'bold') , bg = 'old lace'  , command = lambda : master.switch_frame(MainApp))    
        self.back.grid(row = 0  , column = 0 ) 
        self.ok.grid(row = 2 , column = 2 )    
        self.getvalue = Button(self , text = 'get coordinate') 
    def menubar(self , option ): 
        menubar = controler.Menubar(self , option) 
        return menubar   
    def _check(self ) :  
        global lst  , _pos,Val,_dictval
        list1 = []
        list2 = []
        var = self.entrycoordinate.get()  
        number  = var   
        if(self.entrycoordinate.get() == '' ) :
            try : 
                int(self.entrycoordinate.get()) 
            except ValueError : 
                self.msg = messagebox.showerror("","value is not suitable ") 
        elif(int(self.entrycoordinate.get()) <= 0 ) : 
            self.msg = messagebox.showerror("","value is not suitable ")  
        else : 
            self.labe1 = Label(self , text = "INPUT COORDINATE")  
            self.labe1.grid(row = 5 , column = 1 ) 
            temp = 0 
            for i in range(0 , int(self.entrycoordinate.get())) :  
                self.bt = Entry(self)    
                self.label = Label(self , text =f"{i}" ) 
                self.label.grid(row = i+5  )  
                self.bt.grid(row = i+5  , column = 1  )     
                list1.append(self.bt)    
                temp = i  
            lst = list1  
        self.Getcoordinated = Button(self , text = 'Get coordinated' , command = self.Ok)   
        self.Getcoordinated.grid(row = temp+10 , column = 1   )  
        _pos = temp +10 
    def canvas(self,_lst,l) : 
                global val,k ,temp,_dictval
                global Val 
                lst1 = []  
                temp = _lst 
                _d = []
                lst =  Algorithms._charsym(_lst)
                newindow = Toplevel(self) 
                y =0 
                x = 0  
                self.label = Label(newindow , text = 'Input Parameter'  , font = ('Times' ,'20' ,'bold'))        
                self.label.grid(row = 0 , column =2 )  
                for i in range(0,len(lst)) : 
                    self.label  =Label(newindow , text = f"{lst[i]} : " , font = ('Times' , '9' , 'bold') , bg = 'azure' )
                    self.label.grid(row = i+1, column = 1) 
                    self.entry1 = Entry(newindow , width = 10 , bd = 2) 
                    self.entry1.grid(row = i+1 , column = 2)   
                    lst1.append(self.entry1) 
                    x += i 
                val = lst1  
                k =    lst 
                self.button = Button(newindow, text = 'OK' , command =  self.getval(l))  
                self.button.grid(row = 1 , column = 3)    
                 
    def Ok(self) :  
        global lst ,_pos 
        global Val,_lst
        global l ,count
        _dict = [] 
        d ={}
        self.master.va = lst  
        x = 0    
        y = 0   
        self.button = Button(self , text = " Draw Model " , font = ('calibri' ,'15' , 'bold') , command = self.get) 
        self.button.grid(row = 2 , column = 0 )
        PairCoordinate = []
        for l in lst  : 
            PairCoordinate.append(Algorithms.getString(l.get())) 
        print(l)
        _symlst = Algorithms.splitsym(PairCoordinate) 
        print(_symlst)
        print(PairCoordinate)
        if not Algorithms.checchar(PairCoordinate)  :   
            Newin._create.canvas(self,_symlst)  
            Val = PairCoordinate
            count = 1 
        else  :     
            count = 2 
            Val = PairCoordinate
        _lst = _symlst
    def get(self) : 
        global l  , _lst
        global Val 
        global count 
        k = []
        if(count == 1 ):
         k1 = Newin._create.getval(self,l )  
         k2 = _lst  
         k = Algorithms.replaceVal(k2 , k1 )
        else  : 
            print(Val)
        print(k)
        print(Val) 
        
        # gop cai Val va K thanh mot 
        #ve model  danh dau thanh
        #done
if __name__ == "__main__" : 
    RootAPP = rootapp() 
    RootAPP.mainloop()    
   # print(Algorithms.getString("123"))

        

