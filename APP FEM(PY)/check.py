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
import matplotlib as mlp
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
import solved
import matplotlib.patches as patches

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
    dataArray = graph_data.split('\n') 
    xs=[]
    ys=[]
    zs=[]
    gripx = [] 
    gripy =[] 
    gripz =[]
    xx =[] 
    yy=[]
    xk =np.array([0,0,0,0]) 
    yk =np.array([0,0,0,0])
    count = 0 
    ax1.clear()
    for eachLine in dataArray:
        if ('O' in eachLine ):
                x,y,z = eachLine.split(',')
                xx.append(float(x))  
                yy.append(float(y))  
        elif(len(eachLine)>1 and 'O' not in eachLine and 'M' not in eachLine):
            x,y = eachLine.split(',') 
            xs.append(float(x)) 
            ys.append(float(y)) 
        elif('M' in eachLine )  : 
            x,y,z = eachLine.split(',') 
            gripx.append(float(x)) 
            gripy.append(float(y)) 
    for i in range(0, len(xx), 2):
        ax1.plot(xx[i:i+2], yy[i:i+2], 'wo')
    for i in range (0,len(xx)) : 
         ax1.text(xx[i]+0.01,yy[i]+0.01,f'({int(i+1)})',variant = 'small-caps' )   
    for i in range(0, len(xs), 2):  
        ax1.plot(xs[i:i+2], ys[i:i+2], 'w-') 
    for i in range (0,len( gripx)) :    
        ax1.text(gripx[i]+0.1,gripy[i]+0.1,f'({int(i+1)})',variant = 'small-caps',color='red' )    
    minimum = np.min((ax1.get_xlim(),ax1.get_ylim()))
    maximum = np.max((ax1.get_xlim(),ax1.get_ylim()))

    ax1.set_xlim(minimum*1,maximum*1)
    ax1.set_ylim(minimum*1,maximum*1)
class rootapp(Tk)  : 
    def __init__(self):
        super().__init__()
        self.title("FEM APP") 
        self.grid_propagate(False)
        # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

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
        txt = Text(self)
        global __input
        global count  
        global click  
        global result   
        global draw 
        draw = 0
        result =  0   
        click = False 
        count = 0  
        __input =' '
        self.clicked 
        self.exit_page
        self.style = ttk.Style() 
        self.label1 = Label(self,text="MODEL") 
        self.label1.pack(side = TOP)   
        self.BUttonCo = Button(self,text = 'Command' , command = self.check) 
        self.BUttonCo.pack(side=TOP)
        self.entry = Entry(self) 
        self.entry.pack(side=TOP , fill = BOTH , expand = True) 
        self.entry.bind("<1>" , self.clicked ) 
        self.menuber = controler.Menubar(self,master)  
        self.button = Button(self , text = " Input Coordinate",fg="red", font =("Time",12,"bold"),relief =  GROOVE, command = self. BoxCorrdinate) 
        self.button.pack(side = TOP)  
        self.button1 = Button(self , text = "RESET" ,command = self.reset)  
        self.button1.pack(side = BOTTOM )
        self.Slove = Button(self , text = "Solve" , font=("Time",12,"bold") ,relief =  GROOVE,command = self._solved)  
        self.Slove.pack(side = RIGHT) 
        self.canvas = FigureCanvasTkAgg(f, self) 
        self.canvas.draw() 
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        TextCoordiante = open('ex.txt','a')   
        TextCoordiante.truncate(0)  
        TextCoordiante.close() 
        __input = self.entry 
    def clicked(self,event) : 
        global click 
        click = True 
        print(click)
    def menubar(self , option ) : 
        global txt
        menubar = controler.Menubar(self , option)  
        return menubar    
    def BoxCorrdinate(self) : 
        global txt  
        global count  
        global __input 
        count = 1
        command = __input.get()
        Newindow = Tk() 
        Newindow.label=Label(Newindow , text = " Input CoorDinates") 
        Newindow.label.pack()
        Newindow.tx = Text(Newindow)  
        Newindow.tx['font'] = ('consolas', '12')
        Newindow.tx.pack(expand=True, fill='both') 
        txt = Newindow.tx
        txt.insert(END, 'INPUT DECLARTION{\n\n}\nINPUT NODE{\n\n}\nINPUT COORDINATE {\n\n}\nINPUT FORCES AT POINT AND MOMENT{\nF(x)=[..];\nF(y)=[];\nM=[]\n}\nINPUT FORCES{\n\n}\nINPUT CONSTRAINT{\nconst_x=[Point1,Point2,...];\nconst_y=[];\nconst_angles=[]\n}' )
        Newindow.button = Button(Newindow , text = "OK" , command = self.command)  
        Newindow.button.pack(side = BOTTOM )
        
        Newindow.bind_all('<Control-Key-1>',MainApp.test)
        
    def reset(self) : 
        TextCoordiante = open('ex.txt','a')   
        TextCoordiante.truncate(0)  
        TextCoordiante.close() 
    def exit_page(self,event) : 
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            event.iconify
        return 1
    def draw(self) : 
        pass 
    def command(self) :  
        MainApp.check(self) 
        MainApp.getUip(self)  
    def test(self) : 
        MainApp.check(self) 
        MainApp.getUip(self)  
    def check(self):  
        global _count
        global txt   
        global click
        global __input
        #global symlst
        global ValLst      
        TextCoordiante = open('ex.txt','a')   
        TextCoordiante.truncate(0)  
        TextCoordiante.close() 
        temp = [] 
        temp_=  []
        canvas = Canvas()
        Paircoordinate = []
        _lst = []
        inversion = {}
        middle ={} 
        Forces = []
        lenght = {} 
        command =''      
        retangle = []   
        inputValue=txt.get("2.0",'end-0c')  
        line  =  txt.get("1.0", END).splitlines() 
        line = Algorithms.altho(line) 
        declare = Algorithms.declaration(line[0])
        Paircoordinate = Algorithms.splitText(line[1],0)[0]  
        #print(declare)  
        _symlist = Algorithms.splitsym(Paircoordinate) 
        _symlist = Algorithms._charsym(_symlist) 
        if('O' in _symlist) : 
            _symlist.remove('O')  
        #print(_symlist)
        try : 
            _dict = declare 
            if(len(Algorithms.Find(_dict,_symlist)) != 0 ) : 
                raise FoundException 
            else  : 
                raise RightException 
        except FoundException : 
            k = Algorithms.Find(_dict,_symlist) 
            canvas.msg = messagebox.showerror("",f"value {k}  is not suitable ")      
        except RightException : 
            temp =Algorithms._repval(Paircoordinate,declare) 
        
        Paircoordinate = temp
        GRIP = Algorithms.checkgrip(Paircoordinate)
        Link = Algorithms.LinkPoinr(line[2],Paircoordinate) 
        ForceatPoint = Algorithms.ForcesAtPoint(line[3],-1)[0] 
        #print(Paircoordinate)
        #print(ForceatPoint) 
        #  print(Algorithms.changrCoor(Paircoordinate))
        TextCoordiante = open('ex.txt','a')  
        for i in range(len(Paircoordinate)) :  
                TextCoordiante.write(f"{Paircoordinate[i][0]},{Paircoordinate[i][1]},{'O'}\n")   
        TextCoordiante.close()  
        if(len(Link) > 0) : 
            TextCoordiante = open('ex.txt','a')  
            for i in range(len(Link)) :  
                    TextCoordiante.write(f"{Link[i][0]},{Link[i][1]}\n")   
            TextCoordiante.close()  
        TextCoordiante = open('ex.txt','a')  
        for i in range(len(GRIP )) :   
                TextCoordiante.write(f"{GRIP[i][0]},{GRIP[i][1]},{'O'}\n")   
        TextCoordiante.close()  
        Force = Algorithms.Forces(line[4],Algorithms.Iversion(Link),-1)  
        middle = Algorithms.middle(Link)   
        inversion = Algorithms.Iversion(Link) 
        _val = []
        _val.append(Paircoordinate)  
        TextCoordiante= open('ex.txt','a')
        for i in range(1,len(middle) + 1 ) :  
                TextCoordiante.write(f"{(middle[i])[0]},{(middle[i])[1]},{'M'}\n")    
        TextCoordiante.close()
 
        const =[] 
        const = Algorithms.codeConst(line[5],-1,Paircoordinate)
        angle = [] 
        lenght = Algorithms.distance(Paircoordinate) 
        material = Newin._create.get(self) 
        return(Paircoordinate,inversion,ForceatPoint,Force ,lenght,const,material)
    def getUip(self) :  
        global txt   
        global result
        k = MainApp.check(self)   
        print(k) 
        result = k 
    def _solved(self) : 
        global result 
        window = Toplevel(self)  
        _dict  = solved.Ketqua(result)   
        total_load = (_dict['tl']) 
        total_load = total_load.tolist()
        dof = (_dict['dof'])  
        result = Algorithms.result(total_load,dof) 
        Displacement_vect = (_dict['dv']) 
        Displacement_vect=Displacement_vect.tolist() 
        constraining_focre = _dict['cf']
        internal = (_dict['internal'])
        stress = (_dict['stress'])
        window.LabelLoad = Label(window , text = f' TOTAL LOAD : {total_load}',font =("Time",10,"bold"))  
        window.LabbelDis = Label(window , text =f'Displacement_vect : {Displacement_vect } ' ,font =("Time",10,"bold"))
        window.LabbelCONST = Label(window , text =f'Constraining_focre : {constraining_focre } ' ,font =("Time",10,"bold")) 
        window.internal = Label(window , text =f'Internal : {internal } ' ,font =("Time",10,"bold")) 
        window.LabelLoad.grid(row = 0 , column = 0 , padx = 10 , pady =10 )
        window.LabbelDis.grid(row = 2 , column = 0 , padx = 10 , pady =10 )
        window.LabbelCONST.grid(row = 4 , column = 0 , padx = 10 , pady =10 )
        window.internal.grid(row = 6 , column = 0 , padx = 10 , pady =10 )  
        print(_dict['ts'])
        if ( dof == 2) :   
            stress = (_dict['stress'])
            window.stress = Label(window , text =f'Stress : { stress} ' ,font =("Time",10,"bold"))
            window.stress.grid(row = 8 , column = 0 , padx = 10 , pady =10 ) 
        window.buttonDraw = Button(window , text='DRAW SHEAR FORCES' , font  =("Time",12) ,command = self.draw) 
        window.buttonDraw.grid(row = 10 , column = 2 )   
    def draw(self) : 
        draw = MainApp.check(self) 
        _dict   = solved.Ketqua(draw)   
        solved.diagram(_dict['internal'],_dict['L'],_dict['dof']) 


if __name__ == "__main__" : 
    RootAPP = rootapp() 
    ani = animation.FuncAnimation(f, animate, interval=100) 
    RootAPP.mainloop()     
    

#?L=2,k=3,z=5,q=2 ?(1,k);(1,k*q);(2,3)|(j=2)|(1,2)| (1,2);(2,3)|
#(1,2);(2,2);(2,3)|L(1)=[200]|(j=2)|(1,2)|F(x)=[200,100,200];F(y)=[200,30,900];M=[200,200,300]|Fs(1)=200 
#(1,2,O);(2,3);(8,1) 
""" 
INPUT DECLARTION{

}
INPUT COORDINATE {
(1,2);(9,10);(2,1)
}
INPUT FORCES AT POINT AND MOMENT{

}
INPUT FORCES{
Fs(1)=900
}
INPUT CONSTRAINT{
const_x=[Point1,Point2,...];
const_y=[];
const_angles=[]
}

INPUT DECLARTION{

}
INPUT DECLARTION{

}
INPUT DECLARTION COORSINATE{
(0,0);(2,1);(1,1)
}
INPUT COORDINATE {
(1)-(3);(3)-(2)
}
INPUT FORCES AT POINT AND MOMENT{
F(x)=[0,0,0];
F(y)=[0,0,0];
M=[0,0,0]
}
INPUT FORCES{
Fd(2)=-15000;
Md(1)=15000
}
INPUT CONSTRAINT{
const_x=[1,2];
const_y=[1,2];
const_angles=[1,2]
}

INPUT DECLARTION{
L=1
}
INPUT NODE{
(0,0);(L,0);(L/2,L)
}
INPUT COORDINATE {
(1)-(2);(2)-(3);(3)-(1)
}
INPUT FORCES AT POINT AND MOMENT{
F(x)=[0,0,15000];
F(y)=[0,0,-30000];
M=[0,0,0]
}
INPUT FORCES{
Fd(1)=10000
}
INPUT CONSTRAINT{
const_x=[1];
const_y=[1,2];
const_angles=[1]
}
--------- 
INPUT DECLARTION{

}
INPUT NODE{
(0,2);(0,1);(0,0);(1,1)
}
INPUT COORDINATE {
(1)-(4);(2)-(4);(3)-(4)
}
INPUT FORCES AT POINT AND MOMENT{
F(x)=[0,0,0,10000];
F(y)=[0,0,0,-10000];
M=[0,0,0,0]
}
INPUT FORCES{
Fd(1)=20000
}
INPUT CONSTRAINT{
const_x=[1,2,3];
const_y=[1,2,3];
const_angles=[1,2,3]
}

"""
