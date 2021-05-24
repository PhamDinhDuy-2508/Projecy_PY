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
import tkinter.scrolledtext as scrolledtext 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
try:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import datasheet
style.use('dark_background')
class Error(Exception) : 
    pass   
class FoundException(Error) : 
    pass   
class RightException(Error) : 
    pass  
class EmptyVal(Error) : 
    pass    
class NOTEmptyVal(Error)   : 
     pass  
class recognizeGrip(Error) :  
    pass    
class NotGrip(Error) :
    pass 
f = Figure(figsize=(5,5), dpi=100)
ax1 = f.add_subplot(111) 
def animate(i):
    graph_data = open('ex.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = [] 
    gripx = [] 
    gripy =[]
    middlex = [] 
    middley = [] 
    middlez =[] 
    k = []
    count =  0  
    for line in lines: 
        if len(line) == 3:
            o =  Algorithms.mertext(line).split(',')     
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))  
            
        elif (len(line) == 5 ) : 
            x, y,z = line.split(',')             
            gripx.append(float(x))
            gripy.append(float(y)) 
    try  : 
        Lgripx = len(gripx ) 
        Lgripy = len(gripy)  
        if(Lgripx + Lgripy > 0 )  : 
            raise recognizeGrip  
        else :   
            raise NotGrip
    except recognizeGrip  :    
        ax1.clear()
        ax1.plot(xs, ys,'wo-')      
        ax1.plot(gripx,gripy,'rD') 
        #if (len(middlex) + len(middlez) + len(middley) == 0 ) : 
    except NotGrip :  
        ax1.clear()
        ax1.plot(xs, ys,'wo-')   

    if len(lines) > 5  : 
        for line in lines  : 
            if len(line) > 10  : 
                x, y,z,t = line.split(',')
                middlex.append(float(x))
                middley.append(float(y))   
                middlez.append(float(z)) 
                k.append(t)  
                count += 1 
            if (len(middlex) + len(middley) +len(middlez) == 0 ) : 
                pass 
        for i in range(count):
            k = middlex[i]  
            k2 = middley[i]
            ax1.text(k+0.01,k2+0.01,f'{int(middlez[i])}',variant = 'small-caps' ) 
        for i in range(len(xs)) :  
                ax1.text(xs[i]+0.01,ys[i]+0.01,f'({int(i+1)})',variant = 'small-caps' ) 
class rootapp(Tk)  : 
    def __init__(self):
        super().__init__()
        self.title("FEM APP")
        self._frame = None
        self.switch_frame(MainApp)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        menubar = self._frame.menubar(self)
        self.configure(menu=menubar)
class MainApp(Frame , Newin._create , FoundException):  
    def __init__(self, master ):
        Frame.__init__(self ) 
        global lst   
        global txt
        global click 
        self.style = ttk.Style() 
        self.label1 = Label(self,text="MODEL") 
        self.label1.pack()
        self.menuber = controler.Menubar(self,master)  
        self.button = Button(self , text = " Input Coordinate",fg="red", font =("Time",12,"bold"),relief =  GROOVE, command = self.BoxCorrdinate) 
        self.button.pack()
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw() 
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        TextCoordiante = open('ex.txt','a')   
        TextCoordiante.truncate(0)  
        TextCoordiante.close() 
        self.Slove = Button(self , text = "Slove" , font=("Time",12,"bold") ,relief =  GROOVE )  
        self.Slove.pack(side = TOP )
    def menubar(self , option ) : 
        global txt
        menubar = controler.Menubar(self , option) 
        return menubar   
    def BoxCorrdinate(self) : 
        global txt  
        Newindow = Toplevel(self)   
        Newindow.label=Label(Newindow , text = " Input CoorDinates") 
        Newindow.label.pack()
        Newindow.tx = Text(Newindow) 
        Newindow.tx['font'] = ('consolas', '12')
        Newindow.tx.pack(expand=True, fill='both') 
        txt = Newindow.tx
        Newindow.button = Button(Newindow , text = "OK" , command = self.check_and_Update )  
        Newindow.button.pack(side = BOTTOM )  
    def  check_and_Update(self) :  
        global txt
        print(MainApp.check(self))
        (MainApp.getUip(self))
    def check(self):  
        global txt   
        #global symlst
        global ValLst      
        TextCoordiante = open('ex.txt','a')   
        TextCoordiante.truncate(0)  
        TextCoordiante.close()
        _val = []
        temp = [] 
        temp_=  []
        canvas = Canvas()
        Paircoordinate = []
        _lst = []
        inversion = {}
        middle ={} 
        _Forces = []
        lenght = {} 
        retangle = []
        inputValue=txt.get("1.0","end-1c") 
        if(inputValue[0] == '?') : 
            declaration = Algorithms.declaration(inputValue)
            Paircoordinate = Algorithms.splitText(inputValue ,declaration[1])   
            _symlist = Algorithms.splitsym(Paircoordinate[0]) 
            _symlist = Algorithms._charsym(_symlist) 
            try  : 
                _dict =  declaration[0]   
                if(len(Algorithms.Find(_dict,_symlist)) != 0   ) : 
                    raise  FoundException   
                else : 
                    raise RightException 
            except FoundException   :     
                k = Algorithms.Find(_dict,_symlist)
                canvas.msg = messagebox.showerror("",f"value {k}  is not suitable ")     
            except RightException :  
                arr = []
                lst = (Algorithms._repval(Paircoordinate[0],declaration[0]))   
                TextCoordiante = open('ex.txt','a')   
                TextCoordiante.truncate(0) 
                for i in range(len(lst)) : 
                    TextCoordiante.write(f"{lst[i][0]},{lst[i][1]}\n")  
                TextCoordiante.close()    
            ValLSt = (lst)    
            _val.append(ValLSt )    
            lenght = Algorithms.codeLength(inputValue,Paircoordinate[1])[0]
            pos = Algorithms.codeLength(inputValue,Paircoordinate[1])[1]
            temp  = (Algorithms.Momentcode(inputValue,pos))
            _temp = Algorithms.gripcode(inputValue , temp[1])[0]   
            newpos  =   Algorithms.gripcode(inputValue , temp[1])[1]              
            ForcesANDMomentAtPoint = Algorithms.ForcesAtPoint(inputValue,newpos)             
            Forces = Algorithms.Forces(inputValue ,ValLSt , ForcesANDMomentAtPoint[1]) 
            _Forces.append([ForcesANDMomentAtPoint,Forces])
            #_val.append(temp[0] )
            #_val.append( _temp  ) 
            _val.append( Algorithms. Iversion(_val[0]) )  
            middle = Algorithms.middle(_val[0])  
            TextCoordiante= open('ex.txt','a')
            for i in range(1,len(middle) + 1 ) :  
                TextCoordiante.write(f"{(middle[i])[0]},{(middle[i])[1]},{i},{'O'}\n")    
            TextCoordiante.close()
        else : 
            ValLSt = Algorithms.splitText(inputValue,0) 
            TextCoordiante = open('ex.txt','a')   
            TextCoordiante.truncate(0) 
            _lst = ValLSt[0]    
            declaration = Algorithms.declaration(inputValue)
            lenght = Algorithms.codeLength(inputValue,ValLSt[1])[0]
            pos = Algorithms.codeLength(inputValue,ValLSt[1])[1]
            temp  = (Algorithms.Momentcode(inputValue,pos))
            _temp = Algorithms.gripcode(inputValue , temp[1])[0]              
            newpos  =   Algorithms.gripcode(inputValue , temp[1])[1]  
            ForcesANDMomentAtPoint = Algorithms.ForcesAtPoint(inputValue,newpos)             
            Forces = Algorithms.Forces(inputValue ,_lst , ForcesANDMomentAtPoint[1]) 
            _Forces.append([ForcesANDMomentAtPoint,Forces])
            _val.append(_lst )  
            _val.append( Algorithms. Iversion(_val[0]) )  
            inversion =  Algorithms.Iversion(_lst)  
            for i in range(len(ValLSt[0])) : 
                TextCoordiante.write(f"{_lst[i][0]},{_lst[i][1]}\n") 
            TextCoordiante.close()  
            TextCoordiante = open('ex.txt','a') 
            middle = Algorithms.middle(_val[0])   
            for i in range(1,len(middle) + 1 ) :  
                TextCoordiante.write(f"{(middle[i])[0]},{(middle[i])[1]},{i},{'O'}\n")    
            TextCoordiante.close()
        try : 
            _input = _val  
            if(Algorithms.checkEmpty(_input)) : 
               raise EmptyVal 
            else : raise NOTEmptyVal
        except EmptyVal :  
              canvas.msg = messagebox.showerror("", "lack of parameters")
        except NOTEmptyVal :     
            _l =[] 
            if(len(declaration[0]) != 0  ) :  
                 __l = Algorithms._repval(_temp,declaration[0]) 
                 _temp = __l
            TextCoordiante = open('ex.txt','a') 
            for i in range(len(_temp)) :  
                TextCoordiante.write(f"{_temp[i][0]},{_temp[i][1]},{'O'}\n")  
            TextCoordiante.close()    
        retangle = Algorithms.retangle(_val[0]) 
        
        return (_val,_Forces,lenght,retangle,temp[0]) 
    def getUip(self) :  
        global txt 
        k = [] 
        k = MainApp.check(self)
        controler.Menubar.InformationPage(self,k)  
        print(k)
    # nhan dien toa do trung  
if __name__ == "__main__" : 
    RootAPP = rootapp() 
    ani = animation.FuncAnimation(f, animate, interval=100)
    RootAPP.mainloop()     

#?L=2,k=3,z=5,q=2 ?(1,k);(1,k*q);(2,3)|(j=2)|(1,2)|
#(1,2);(2,2);(2,3)|L(1)=[200]|(j=2)|(1,2)|F(x)=[200,100,200];F(y)=[200,30,900];M=[200,200,300]|Fs(1)=200