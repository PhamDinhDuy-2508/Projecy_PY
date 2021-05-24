from tkinter import * 
import Algorithms
import pandas as pd  
import sys  
import os 
import datasheet 
#import test  
from tkinter  import ttk
from tkinter import messagebox   
#from tkinter.ttk import *
class _create:   
    def __init__(self, master):
        Frame.__init__(self, master)
        super().__init__()  
        global _dict 
        self.key = 0     
        global value  
        value = []
        self.k1 =  list() 
        k1 = self.k1 
        self.get(self , k1 )
        self.getInformation(self,event) 
        self.materialPage(self ,lst )  
        self._LLST ={}
        self.getLLST(self,_LLST)
        self.getval(self,self.k1)
    def canvas(self,_lst) : 
        global val,k ,temp,_dictval,_dict
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
        self.button = Button(newindow, text = 'OK' , command =  self.getval )  
        self.button.grid(row = 1 , column = 3)        
    def getval(self)  :
            global k,temp , val,_dictval,_dict
            k2 = []
            Arr = []
            DictVal={}    
            for i in range(len(val))  :  
                DictVal.__setitem__(k[i] , (val[i].get())) 
            DictVal['E'] = str(float(DictVal['E']))
            return DictVal
    def Component(self , s ) : 
            Newindow = Tk()
            newindow.config(bg = 'white') 
             
    def get(self,k)        :   
     k = self.getval(k)
     return k 
    def _warning(self  )  :   
        global k 
        k = k+1  
        return ( k )   
    def informationPage(self,s) :    
        k.append(s)
        return k
    def materialPage(self ,lst ) :    
        global listbox 
        global value
        newindow = Tk()         
        var3 = StringVar() 
        ArrofMaterial = []
        listbox = Listbox(newindow, listvariable = var3)  
        newindow.title("Material Page")  
        newindow.geometry('500x300') 
        newindow.config(bg = 'white')
        newindow.lb1 = Label(newindow , text ='Material Menu' , font = ('Arial' , 15 ) , width = 20  , relief = RIDGE )  
        newindow.buttonApply= Button(newindow , text='Apply' , font= ('Time',12),command =self.getdatafromBase) 
        newindow.buttonOk= Button(newindow , text='OK' , font= ('Time',12) ) 
        newindow.buttondelete = Button(newindow , text ='DELETE' , font = ('Time',12) ,command = self.deteteDATA)
        newindow.buttonCreate = Button(newindow , text = 'Create new Material' , font = ('Time' , 12) ,command = self._createnewMaterial)  
        list_items = datasheet.DataOfMaterial()  
        if lst != ' ' : 
             listbox.insert(END , lst)  
             list_items.append(lst)
        for i in list_items : 
            listbox.insert('end' , i )  
        newindow.lb1.pack()   
        scroolbar = Scrollbar(newindow)  
        listbox.pack( fill =BOTH, expand = 2 )      
        listbox.bind("<Double-Button-1>" , self.getInformation) 
        listbox.bind('<Button-3>' , self.rightkick)
        scroolbar.pack(side = RIGHT , fill = Y, expand = 1 )
        newindow.buttonApply.pack(side = LEFT, expand = True, fill = BOTH , padx = 10 ) 
        newindow.buttonOk.pack(side = LEFT, expand = True, fill = BOTH , padx = 10 )    
        newindow.buttonCreate .pack(side = LEFT, expand = True, fill = BOTH , padx = 10 )  
        newindow.buttondelete.pack(side = LEFT, expand = True, fill = BOTH , padx = 10 ) 
    def _createnewMaterial(self) : 
        global k , listbox ,value
        newindow = Toplevel(self)  
        var = StringVar() 
        VarP = StringVar() 
        VarV = StringVar()  
        VarA =  StringVar() 
        VarM = StringVar()
        lst = [] 
        newindow.BUttonOke = Button(newindow , text = 'Ok'  , relief = GROOVE  , width = 7 , command = self.getdata )  
        newindow.label= Label(newindow , text ='________Create new Material________ '  , font = ('Time' ,16 ))    
        newindow.labelName = Label(newindow , text = 'Name of material : ')   
        newindow.labelPosoin =  Label(newindow , text = ' Indices Poissoin : ') 
        newindow.labelV =   Label(newindow , text = 'Moment Of Inertia : ') 
        newindow.entryName = Entry(newindow , textvariable = var  )    
        newindow.entryP = Entry(newindow , textvariable =  VarP  )     
        newindow.entryv = Entry(newindow , textvariable =  VarV  )                 
        newindow.A = Entry(newindow , textvariable = VarA )  
        newindow.LabelA = Label(newindow, text = "cross-section area : ")  
        newindow.LabelMoment = Label(newindow , text = "Moment of inertia : ") 
        newindow.entryMoment =  Entry(newindow , textvariable = VarM)
        newindow.label.grid(row = 0 , column = 1 , pady = 10   )  
        newindow.labelName.grid(row = 1 , column  = 0  , pady = 10 ) 
        newindow.entryName.grid(row = 1 , column = 1  , pady = 10  ) 
        newindow.entryP.grid(row = 2 , column =  1 , pady = 10 ) 
        newindow.labelPosoin.grid(row = 2 , column =  0 , pady = 10  ) 
        newindow.labelV.grid(row = 3 , column = 0 ,pady = 10  )   
        newindow.entryv.grid(row = 3 , column = 1 ,pady = 10 )  
        newindow.BUttonOke.grid(row = 5 , column = 4   )      
        newindow.A.grid(row = 4 , column = 1 ) 
        newindow.LabelA.grid(row = 4 , column =  0 ) 
        lst = [newindow.entryName , newindow.entryP , newindow.entryv,newindow.A]   
        k = lst  
    def getdata(self) :  
        global k  , listbox   
        global value 
        val = k[0].get()
        listbox.insert(END , val ) 
        _object = open('database.txt','a')  
        _object.write(f"{k[0].get()},{k[1].get()},{k[2].get()},{k[3].get()}\n")
        _object.close()   
        value.append([{k[0].get()},{k[1].get()},{k[2].get()},{k[3].get()}])

    def getInformation(self , event):  
        global listbox    
        global k 
        global value   
        k = 0   
        check = 0 
        _dict ={}
        data = listbox.get(listbox.curselection()) 
        _dict = datasheet.GetDict()  
        _var1 = StringVar() 
        _var2 = StringVar() 
        _var3 = StringVar() 
        _var4 = StringVar()
        _var1.set(data)
        _var2.set(_dict[data][0] )
        _var3.set(_dict[data][1]) 
        _var4.set(_dict[data][2])
        newindow =  Toplevel(self )   
        newindow.config(bg  = 'white') 
        newindow.title("INFORMATION") 
        newindow.labek = Label(newindow, text=' Name Of Material: ' , font = ('Arial' , 12 ) , bg = 'white') 
        newindow.LabelOfpoison = Label(newindow , text = 'Poison Incides : ' , font = ('Arial' , 12 ) ,bg = 'white')  
        newindow.labelMAtre = Label(newindow , text ='Moment Of Inertia : ',font = ('Arial' , 12 )  , bg = 'white' )     
        newindow.entry1 = Entry(newindow , textvariable = _var1 ) 
        newindow.entry1.grid(row = 0 , column = 1 ) 
        newindow.entry2 = Entry(newindow , textvariable = _var2   ) 
        newindow.entry2.grid(row = 1 , column = 1 ) 
        newindow.entry3 = Entry(newindow , textvariable = _var3,  )  
        newindow.entry3.grid(row = 2 , column = 1 ) 
        newindow.labek.grid(row = 0 , column = 0 )  
        newindow.LabelOfpoison.grid(row = 1 , column = 0 )  
        newindow.labelMAtre.grid(row = 2 , column = 0 )    
        newindow.entry4 = Entry(newindow , textvariable = _var4,  )  
        newindow.entry4.grid(row = 3 , column = 1 )  
        newindow.label4 = Label(newindow , text = "Cross-Section Area : " ,font = ('Arial' , 12 )  , bg = 'white' )  
        newindow.label4.grid(row = 3 , column = 0 ) 
        newindow.buttonUPdate = Button(newindow , text = 'OK' , width = 5 ,command = self.getDATABASE  )  
        newindow.UPdate = Button(newindow ,text = 'UPDATE'  ,command =  lambda : self._warning())    
        newindow.buttonUPdate.grid(row = 4 , column = 1  )  
        newindow.UPdate.grid(row = 4 , column = 0  )    
        value = [_var1,_var2,_var3,_var4] 
    def getDATABASE(self) : 
        global value
        for i in range(len(value)) : 
            print(value[i].get())
    def deteteDATA(self) : 
        global listbox  
        _delete = listbox.curselection() 
        for i in  reversed(_delete) : 
            listbox.delete(i)
    def rightkick(self,event) :   
        newindow = Menu(self,tearoff = 0 )  
        newindow.add_command(label='Delete', command=self.delete) 
        newindow.add_command(label='Show information', command=self.getInformation)  
        newindow.add_separator() 
    def getdatafromBase(self) : 
        global listbox
        global value
        _dict ={}
        data = listbox.get(listbox.curselection()) 
        _dict = datasheet.GetDict()  
        _var1 = StringVar() 
        _var2 = StringVar() 
        _var3 = StringVar() 
        _var4 = StringVar()
        _var1.set(data)
        _var2.set(_dict[data][0] )
        _var3.set(_dict[data][1]) 
        _var4.set(_dict[data][2])
        value = [_var1,_var2,_var3,_var4] 
        value=  ( value[0].get(),value[1].get(),value[2].get(),value[3].get() )  
        print(value)
    def get(self) :  
        global value
        _dict = {'A':value[3],'E':value[1],'J':value[2]} 
        return _dict 


