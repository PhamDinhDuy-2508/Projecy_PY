# vì mùa bài tập lớn + mùa thi nên nhóm em chỉ kịp update option làm định nghĩa các hằng số khác ngoài x ,y z , không kịp làm phần virtual keyboard  
# vd như D,L,k,q,w ,e, i..................... trong hộp thoại có tên là command line >>>>> 
# và có thể giải được đề giữa kì r ạ  
# vì không đủ thời gian làm phần virtual keyboard nên nhóm em rất tiếc vì phải thiếu chức năng này 
# vì thời gian hoàn thành hơi gấp nên chức năng mới của nhóm em  là command line >>> có nhiều chỗ chưa được hoàn chỉnh và chưa được tự động hóa hoàn toàn  ,  mong thầy thông cảm ạ 
# nếu được nhóm em xin nộp thầy bản này trước còn option virtual keyboard thì khoảng sau thi nhóm em sẽ nộp tiếp cho thầy ạ !
from tkinter import *  
from tkinter import ttk 
from tkinter import messagebox
import numpy as np
import math as mth
import matplotlib.pyplot as mlp
from sympy import *  
from sympy.parsing.sympy_parser import parse_expr    
import sys   
import string              
sys.getdefaultencoding()   
class Exceptionnew (Exception) : 
    pass  
class ValueException(Exceptionnew)  : 
    pass  
class NullException( Exceptionnew ) : 
    pass 
class valueException(Exception):  
    def __init__(self , value) : 
        super().__init__() 
        self.value = value    
class NULLExpction() : 
    pass
class SpecialAlpha(Exceptionnew) : 
    pass
class Stack : 
    def __init__(self):
        self.arr = [] 
        self.top = -1 
        self.predencen = {"(" : 1  ,"+":2 ,"-" : 2 , "*" : 2 , "/" : 2 , "^" : 3 , "sqrt" : 4  } 
    def empty(self) :
        return self.arr == []
    def pop(self) :  
        if self.empty() : 
            return None 
        self.top -= 1 
        return self.arr.pop() 
    def Push(self , val) : 
        self.arr.append(val) 
        self.top += 1 
    def peek(self) :  
        return self.arr[len(self.arr) -1 ]   
def checkNumber(s) :
    try : 
        float(s) 
        return True 
    except ValueError : 
        return False 
def tokenNumber(s) :     
    _char = [] 
    _crash= []
    while(s) : 
        if s[0] in "0123456789": 
            number = s[0]
            s = s[1:] 
            while(s  and  s[0] in "0123456789.") :  
                number += s[0] 
                s = s[1:] 
            _char.append(number) 
            if s : 
                _crash.append(s[0]) 
                s = s[1:]
    return _char
def __tokensize(s) :  
    _char = [] 
    while(s) : 
        if s[0] in "-0123456789": 
            number = s[0]
            s = s[1:] 
            while(s  and  s[0] in "-0123456789.") :  
                number += s[0] 
                s = s[1:] 
            _char.append(number) 
            if s : 
                _char.append(s[0]) 
                s = s[1:] 
        elif s[0] in "sqrt" : 
            _str = s[0] 
            s= s[1:] 
            while(s and s[0] in "sqrt") : 
               _str += s[0] 
               s = s[1:] 
            _char.append(_str) 
            if s : 
                _char.append(s[0]) 
                s = s[1:]  
        else : 
            _char.append(s[0]) 
            s = s[1:] 
    return _char   
def tokenfunc(s) : 
    _char = []   
    _Str ="" 
    mylistt = [chr(chnum) for chnum in list(range(ord('a') , ord('z') +1)) ]
    for i in mylistt :  
        _Str += i  
    _Str= _Str+"-0123456789." +_Str.upper()
    while(s):
        if s[0] in _Str : 
           _ch = s[0] 
           s = s[1:]  
           while(s and s[0] in (_Str)  ): 
               _ch += s[0] 
               s= s[1:] 
           _char.append(_ch) 
           if s : 
               _char.append(s[0])  
               s= s[1:]
        else : 
            _char.append(s[0]) 
            s = s[1:]     
    return _char 
def _command(_s) : 
    _s = __tokensize(_s)  
    _S = [] 
    _S1= []
    for i in _s  : 
        if checkNumber(i) :  
            _S.append(i) 
        else : 
            if i.isalpha() : 
                _S1.append(i)
            else : 
                pass
    return dict(zip(_S1,_S)) 
    value_dict = dict(zip(_S1 , _S2)) 
def __tokenexponentia(s) :  
     _char = [] 
     while(s) : 
        if s[0] in "**": 
            number = s[0]
            s = s[1:] 
            while(s  and  s[0] in "**") :  
                number += s[0] 
                s = s[1:] 
            _char.append(number) 
            if s : 
                _char.append(s[0]) 
                s = s[1:] 
        else : 
            _char.append(s[0]) 
            s = s[1:] 
     return _char     
def InfixtoPofix(Infix) : # hàm chuyển đổi tiền tố hậu tố để tính toán biểu thức này ở dưới em đã có hàm eval() thay thế nên sẽ gọn hơn nhưng muốn  thêm kí hiệu toán học theo yêu cầu của người dùng muốn thêm vào thì sẽ phải dùng thuật toán này 
                        # ví dụ muốn  thêm  những kí hiệu toán học mà người dùng tự định nghĩa (như căn bậc 3 : Sqrt_3() , căn bậc n :sqrt_(n)(.....) ,ln() ) thì sẽ phải dùng thuật toán balan này để phát triển lên 
                        # hay sử dụng bàn phím ảo thì  cũng sẽ phải dùng thuật toán balan này để phát triển lên vì sẽ có 1 số kí tự không nằm trong thư viện sympy trong python
    Newstack = Stack() 
    _Infix = []
    Pofixarr = __tokensize(Infix)  
    i = 0 
    if Pofixarr[0] == '-' and Pofixarr[i+1] == '(': 
        Pofixarr.remove(Pofixarr[0])
        Pofixarr.insert(0 , '*') 
        Pofixarr.insert(0 , '-1')
    #print(Pofixarr)
    for token in Pofixarr : 
        if checkNumber(token): 
            _Infix.append(token) 
        elif token == '(' : 
            Newstack.Push(token)
        elif token == ')' : 
            Poptop = Newstack.pop() 
            while Poptop != '('  and not Newstack.empty() : 
                _Infix.append(Poptop) 
                Poptop = Newstack.pop()  
        else : 
            if ( (token == '-' and Pofixarr[i-1] in "+-*/" and Pofixarr[i+1].isdigit())) :   
                if __tokensize(token) : 
                    _Infix.append(token)
            elif ( token == '-' and i == 0  and Pofixarr[i+1] == '(') : 
                        pass
            while not Newstack.empty() and Newstack.predencen[token] <= Newstack.predencen[Newstack.peek()] : 
                 _Infix.append(Newstack.pop()) 
            Newstack.Push(token) 
        i += 1 
    while not Newstack.empty(): 
            _Infix.append(Newstack.pop()) 
    return " ".join(_Infix)
class EvalPofix  : #tính toán hậu tố  dựa vào thuật toán balan ở trên 
    def __init__(self): 
        self.stack =[] 
        self.top =-1
    def pop(self): 
        if self.top ==-1: 
            return
        else: 
            self.top-= 1
            return self.stack.pop() 
    def push(self, i): 
        self.top+= 1
        self.stack.append(i)  

    def centralfunc(self, ab): 
        Temp_stack = [] 
        for i in ab: 
            if ( i != '+' and i != '-' and i != '*' and i != '/' and i != '^' and i != 'sqrt'):  
                    self.push(float(i))
            else : 
                if (i == '+') : 
                    val1 = self.pop()
                    val2 = self.pop()
                    result = val1+val2 
                    self.push(result)
                elif( i == '-') : 
                    val1 = self.pop()
                    val2 = self.pop()
                    result = val2 - val1
                    self.push(result)  
                elif ( i == '*') : 
                    val1 = self.pop()
                    val2 = self.pop()
                    result = val1*val2 
                    self.push(result)
                elif ( i == '/') : 
                    val1 = self.pop()
                    val2 = self.pop()
                    result = val2 / val1 
                    self.push(result)
                elif ( i == '^') : 
                    val1 = self.pop()
                    val2 = self.pop()
                    result = val1**val2
                    self.push(result)
                elif ( i == 'sqrt') : 
                    result = mth.sqrt(self.pop())
                    self.push(result)
        return float(self.pop())   
def change(s): 
    _s = __tokenexponentia(s)
    _ss =''
    for i in range(len(_s)) : 
        if(_s[i] == '**') : 
            _s[i]='^' 
        _ss += _s[i]
    return(_ss) 
def _change(s) : 
    return(s.replace('^' ,'*'+'*'))
def _Dervaluex(s) :  
    list1 = []
    temp = [] 
    Zingmatemp = [temp]
    _Func =''
    specialChar = ['+' , '-' , '*' ,'/' , 'sqrt']
    _strFunc =''
    symbols_x = {'x' : Symbol('x' , real = True)} 
    symbols_y = {'y' : Symbol('y' , real = True)} 
    symbols_z = {'z' : Symbol('z' , real = True)}
    resultx = parse_expr(s , symbols_x)
    resulty = parse_expr(s , symbols_y) 
    resultz = parse_expr(s , symbols_z) 
    _L1 =  diff(resultx , symbols_x['x'])     
    _L2 = diff(resulty , symbols_y['y']) 
    _L3 = diff(resultz , symbols_z['z']) 
    list1 = [_L1 , _L2 ,_L3] 
    i = 0  
    j = 0 
    for Tken in list1  : 
        k = []
        k = str(Tken).split(' ') 
        pos = []
        treatment = []
        i =0 
        j = 0 
        for token in k  :         
            if token in specialChar : 
                pass  
            else : 
                k[i]= '0'
                _func = (token)
                for _token in _func :
                        treatment.append(_token) 
                func=_func[::-1] 
                #print(_func)
                for j in range(len(func)) : 
                    k.insert(i,func[j])
            
                k.remove('0')  
            i+=1  
        Zingmatemp[j].append(k)  
        j += 1 
    return temp
def _replaceValuex(value, s) : 
    charList = ['x','y','z'] 
    _s =''
    _k= []
    _str =''
    k = [] 
    temp = []
    for i in range(0 , len(value) ) :  
        _s =''
        for j in range(len(s[i])):
            _k =''
            _s += s[i][j]
        temp.append(_s)
    k.clear()
    i = 0 
    j = 0
    x  =1
    y = 1 
    z =1
    while (i<3  ) : 
        s= temp[i]
        j = 0
        while( x+y+z!=0 or j < 3)  : 
            if (j < 3) :
                s =s.replace(charList[j],value[j]) 
                x = s.count('x') 
                y = s.count('y') 
                z = s.count('z')
                j +=1
            else : 
                continue
        i +=1
        k.append(s)
    for i in range(len(k)) : 
       k[i] = (change(k[i]))
    return k
def ZIgmachange(s) : 
    _str =''
    _str1=''
    temp =[]
    _temp = []
    _temp2 = []
    _s = _change(s)
    temp = _Dervaluex(_s)
    for i in range (len(temp)):  
        _str =''
        for j in range(len(temp[i])) : 
          _str += temp[i][j]
        _temp.append(_str) 
    temp.clear()  
    _strr =' '
    for i in range (len(_temp)) : 
       temp.append(change(_temp[i]))
    return temp
def _replacespecial(s,_dict) :  
    i = 0  
    for i in range(len(s)) : 
        for j in range(len(s[i])) : 
            if s[i][j] in (string.ascii_lowercase[0:23] +string.ascii_uppercase[0:23] ) : 
                k = _dict[s[i]]
                s.remove(s[i]) 
                s.insert(i,k) 
    return s 
class rootapp(Tk):
    def __init__(self):
        super().__init__()
        self.title("TENSOR APP")
        self._frame = None
        self.switch_frame(MainApp)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class MainApp(Frame):  
    def __init__(self, master ):
        Frame.__init__(self , master ) 
        super().__init__() 
        Frame.config(self , bg = 'white' , width = 100)
        Frame(self , width = 200 , height = 200)
        self.Label1 = Label(self , text = 'LỰA CHỌN CHỨC NĂNG' , font = ('Times' , 20 , 'bold') , bg = 'LightBlue3' , relief = RAISED ) 
        self.Label1.grid(row = 0  , column = 1 )  
        self.Button1 = Button(self , text = "Tính Tensor ma trận" , font = ('calibri' , 12 , 'bold')  ,bg = 'LightSteelBlue2', command = lambda : master.switch_frame(Page1_frame)) 
        self.Button1.grid(row = 1 , column = 1  , padx =10 , pady = 10 )  
        self.Button2 = Button(self , text = "Bài Toán Trường Chuyển Vị" , font = ('calibri' , 12 , 'bold'),bg = 'LightSteelBlue2'  , command = lambda : master.switch_frame(Derapp)) 
        self.Button2.grid(row = 2 , column = 1 , padx = 10 , pady = 10)  
        self.Button3= Button(self , text = "Tính Biến Dạng" , font = ('calibri' , 12 , 'bold') , bg = 'LightSteelBlue1',command = lambda : master.switch_frame(Page1_Frame6)) 
        self.Button3.grid(row =3 , column =1 , padx = 10 , pady = 10 )
class Derapp(Frame) : 
    def __init__(self, master, *args, **kwargs): 
        Frame.__init__(self, master, *args, **kwargs) 
        super().__init__(*args, **kwargs)
        self.var1 =' '
        self.var2 =' '
        self.Label1 = Label(self , text = 'Trường Chuyển Vị' , font = ('Times' , 18 , 'bold' ) , fg = 'white', bg = 'blue2') 
        self.Label1.grid(row = 0 , column = 1  , padx = 20 , pady = 20 ) 
        self.Label2 = Label(self , text = 'U_1 = ' , font = ('Times' , 14 , 'bold'))  
        self.Label2.grid(row = 1 , column = 0 )
        self.entry1 = Entry(self , width = 70 , bd = 1 , textvariable = self.var1 ) 
        self.var1 = set(self.entry1.get())
        self.entry1.grid(row = 1 , column =  1  , padx = 10 , pady = 10  )  
        self.label3 = Label(self , text = 'U_2 = ' , font = ('Times' , 14, 'bold'))  
        self.label3.grid(row = 2 , column =  0)
        self.entry2 = Entry(self , width = 70 , bd = 1, textvariable = '__2') 
        self.var2 = set(self.entry2.get())
        #muon entry1 va entry cung dc nhap thi self.entry2 = Entry(self , width = 70 , bd = 1, textvariable = self.var1) 
        self.entry2.grid(row  = 2 , column = 1  , padx = 10 , pady = 10) 
        self.entry3 = Entry(self , width =70 , bd = 1  ,textvariable = '__1' ) 
        self.Label3 = Label(self ,text = 'U_3 = ' , font = ('Times' , 14, 'bold') ) 
        self.Label3.grid(row = 3 , column  = 0 ) 
        self.entry3.grid(row = 3 , column = 1 ) 
        self.button = Button(self , text = 'Quay lại Menu' , font =('calibri' , 12 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda : master.switch_frame(MainApp)) 
        self.button.grid(column  = 1 , row = 5) 
        self.button1 = Button(self , text = 'Tính biến dạng' ,font =('calibri' , 12 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = self.switch_frame)
        self.button1.grid(column  = 1 , row = 4) 
        var1 = self.entry1.get() 
        var2 = self.entry2.get() 
        var3 = self.entry3.get()
    def switch_frame(self) : 
       _var1 = self.entry1.get() 
       _var2 = self.entry2.get() 
       _var3 = self.entry3.get() 
       self.master.var1 = _var1 
       self.master.var2 = _var2 
       self.master.var3 = _var3
       self.master.switch_frame(resultOFDerFrame) 
"""class _Canvas(_Frame) : 
    def __init__(self ):
        super().__init__()  
        self._cvs = Canvas(self , height = 300 , width = 300 ) 
        self._cvs.pack()"""
class resultOFDerFrame(Frame):   
    def __init__(self, master, *args, **kwargs): 
        
        Frame.__init__(self, master, *args, **kwargs) 
        super().__init__(*args, **kwargs) 
        Frame.config(self , bg = 'white' , width = 100) 
        global username 
        global _global1 ,_global2
        global val
        self.var1 = (self.master.var1)
        self.var2 = (self.master.var2)
        self.var3 = (self.master.var3)  
        self._var1 = _Dervaluex(_change(self.var1))
        self._var2 = _Dervaluex(_change(self.var2)) 
        self._var3 = _Dervaluex(_change(self.var3)) 
        self.label1 = Label(self , font =('Times' ,12 , 'bold') , bg = 'Snow' , relief = GROOVE)
        self.label1.grid(row = 1 , column = 3 )  
        self.label1['text'] = 'U_1' + '=' +  self.var1   
        self.label2 = Label(self , font =('Times' ,12 , 'bold') , bg = 'Snow' , relief = GROOVE)
        self.label2.grid(row = 2 , column = 3)  
        self.label2['text'] ='U_3' + '=' + self.var2 
        self.label3 = Label(self , font =('Times' ,12 , 'bold') , bg = 'Snow' , relief = GROOVE)
        self.label3.grid(row = 3 , column = 3 )  
        self.label3['text'] ='U_3' + '=' + self.var3
        self._label = Label(self  , text = 'Biến Dạng Tương Ứng' , font = ('calibri' , 14 , 'bold'  ) ,fg = 'white', bg = 'blue2') 
        self._label.grid(row = 4 , column =3 )
        self._label1 = Label(self  , text = 't11 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label1.grid(row = 5 , column =0)
        self._label2 = Label(self  , text = 't12 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label2.grid(row = 5 , column =2)
        _functionVar = (self.var1 , self.var2 , self.var3) 
        self._Varlabel1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel1['text'] =  ZIgmachange(self.var1)[0] 
        self._Varlabel1.grid(row = 5 , column =1)
        self._Varlabel2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE) 
        self._Varlabel2.grid(row = 5 , column =3)
        self._Varlabel2['text'] = (str(0.5))+'('+ZIgmachange(self.var1)[1]+'+'+ZIgmachange(self.var2)[0]  +')'
        self._label3 = Label(self  , text = 't13 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label3.grid(row = 5 , column =4)
        self._Varlabel3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel3['text'] = (str(0.5))+'('+ZIgmachange(self.var1)[2] +'+'+ZIgmachange(self.var3)[0]+')'
        self._Varlabel3.grid(row = 5 , column =5) 
        self._label4 = Label(self  , text = 't21 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label4.grid(row = 6 , column =0 )
        self._Varlabel4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel4['text'] = (str(0.5))+'('+ZIgmachange(self.var1)[1]+'+'+ZIgmachange(self.var2)[0] +')'
        self._Varlabel4.grid(row = 6 , column = 1 ) 
        self._label5 = Label(self  , text = 't22 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label5.grid(row = 6 , column =2 )
        self._Varlabel5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel5['text'] =  ZIgmachange(self.var2)[1] 
        self._Varlabel5.grid(row = 6 , column = 3 ) 
        self._label6 = Label(self  , text = 't23 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label6.grid(row = 6 , column =4 )
        self._Varlabel6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel6['text'] =(str(0.5))+'('+ZIgmachange(self.var3)[1]+'+'+ZIgmachange(self.var2)[2]+')'
        self._Varlabel6.grid(row = 6 , column = 5 ) 
        self._label7 = Label(self  , text = 't31 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label7.grid(row = 7 , column = 0 )
        self._Varlabel7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel7['text'] =(str(0.5))+'('+'('+ZIgmachange(self.var1)[2]+')'+'+'+'('+ZIgmachange(self.var3)[0]+')' +')'
        self._Varlabel7.grid(row = 7 , column = 1 ) 
        self._label8 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label8.grid(row = 7 , column = 2 )
        self._Varlabel8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel8['text'] =(str(0.5))+'('+ZIgmachange(self.var3)[1]+'+'+ZIgmachange(self.var2)[2] +')'
        self._Varlabel8.grid(row = 7 , column = 3 ) 
        self._label9 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label9.grid(row = 7 , column = 4 )
        self._Varlabel9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel9['text'] = ZIgmachange(self.var3)[2] 
        self._Varlabel9.grid(row = 7 , column = 5 ) 
        self.button = Button(self , text = 'Quay lại Menu' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda : master.switch_frame(MainApp)) 
        self.button.grid(column  = 5 , row = 0 )  
        self.Label1 = Label(self , text = 'x = ' , font = ('calibri' , 12 , 'bold')  , relief = GROOVE  ) 
        self.entry1 = Entry(self ,  bg = 'whitesmoke' , textvariable = '_1')  
        self.Label1.grid(row = 8 , column = 0 ) 
        self.entry1.grid(row = 8  , column = 1)
        self.Label2 = Label(self , text = 'y = ' , font = ('calibri' , 12 , 'bold')  , relief = GROOVE  ) 
        self.entry2 = Entry(self ,  bg = 'whitesmoke',  
        textvariable = '_2')  
        self.Label2.grid(row = 8 , column = 2 ) 
        self.entry2.grid(row = 8  , column = 3 )         
        self.Label3 = Label(self , text = 'z = ' , font = ('calibri' , 12 , 'bold')  , relief = GROOVE  ) 
        self.entry3 = Entry(self ,  bg = 'whitesmoke' , textvariable ='_5')  
        self.Label3.grid(row = 8 , column = 4 ) 
        self.entry3.grid(row = 8  , column = 5)        
        self.Button1 = Button(self , text = 'Trở lại trang trước' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda : master.switch_frame(Derapp)) 
        self.Button1.grid(row = 0 , column = 0 )
        lisk = [ZIgmachange(self.var1)[0] ,ZIgmachange(self.var1)[1]  , ZIgmachange(self.var1)[2] , ZIgmachange(self.var2)[0] ,ZIgmachange(self.var2)[1]  , ZIgmachange(self.var2)[2] , ZIgmachange(self.var3)[0] ,ZIgmachange(self.var3)[1]  , ZIgmachange(self.var3)[2]]  
        self.button2 = Button(self ,text ='Tính trường biến dạng' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = self.ADDframe  ) 
        self.button2.grid(row = 9 , column = 3 )
        self.button3 = Button(self , text = 'command line >>>>>' ,font =('calibri' , 9 , 'bold') ,bg = 'ivory3', command = self._canvas)
        self.button3.grid(row = 3 , column = 0 ) 
        temp = []
        countx = 0  
        county = 0 
        countz = 0 
        for  i in range(len(lisk) ) : 
                countx += lisk[i].count('x') 
                county += lisk[i].count('y')
                countz += lisk[i].count('z')   
        temp.append(countx) 
        temp.append(county) 
        temp.append(countz) 
        countx = temp[0]
        county = temp[1] 
        countz = temp[2] 
        if countx == 0 : 
            self.entry1.config(state = 'disabled')
            if (county == 0 ) : 
                self.entry2.config(state = 'disabled')
                if countz ==0 : 
                    self.entry3.config(state = 'disabled') 
            else :  
                if countz == 0 : 
                    self.entry3.config(state = 'disabled')
        else : 
            if (county == 0 ) :  
                self.entry2.config(state = 'disabled')
                if countz ==0 : 
                    self.entry3.config(state = 'disabled')
            else :  
                if countz == 0 :
                    self.entry3.config(state = 'disabled')  
        temp.clear()
        #value = ['1','2','3'] 
        v1 = self.entry1.get()
        v2 = self.entry2.get() 
        v3 = self.entry3.get() 
        _global2 = 0
    def _canvas(self) :   
        global val
        global _global1 , global2
        newindow = Toplevel(self)   
        _var = StringVar()
        _var.set('0')
        self.label = Label(newindow , text = 'Nhập command Line >>>> ' )   
        self._entry = Entry(newindow , width = 70  ,  bd = 1, textvariable = _var) 
        self._entry.grid(row =  0  , column = 2 ) 
        self.label.grid(row = 0 , column  = 1 )      
        self.button3 = Button(newindow , text = 'OK'  ,  font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE  ,  command = lambda : self._print() ) 
        self.button3.grid(row = 1 , column = 1)
        val  = (self._entry.get()) 
        _global2 = 1 
    def _print(self) : 
            _global1 =''
            global _global2
            _v1 = self._entry.get() 
            self.master.val = _v1
            self.v1 = self.master.val
            try : 
                if self._entry.get()  == ''  : 
                    raise NullException   
                else : 
                    raise ValueException
            except ValueException : 
                self.v1 = self._entry.get() 
            except NullException:  
                self.v1 = '0'
            self.master.val1  = self.v1 
            _global1 = (_command(self.master.val1)) 
            _global2 = 1 
            return( _global1)
    def ADDframe(self) :
        global _global1 
        global _global2
        global username  
        print(self._var1)
        _v1 = self.entry1.get()
        _v2 = self.entry2.get()
        _v3 = self.entry3.get()
        self.master.v1 = _v1 
        self.master.v2 = _v2 
        self.master.v3 = _v3
        if _global2 == 1 :
             _global1 =self._print()
             for  i in range(0,3) : 
                 self._var1[i] = _replacespecial(self._var1[i] , _global1)   
                 self._var2[i] = _replacespecial(self._var2[i] , _global1) 
                 self._var3[i] = _replacespecial(self._var3[i] , _global1)
        else : 
            pass  
        _value=[self.master.v1,self.master.v2,self.master.v3]
        for i in range (len(_value)) :  
            if _value[i] == '' : 
                _value[i] = '0' 
        for i in range(len(_value)): 
            _value[i] = str(eval(_value[i]))
        value = []
        for i in range(len(_value)) : 
            if _value[i] != '' : 
                value.append(_value[i]) 
            else : 
                value.append('0') 
        self.a = np.arange(9).reshape(3, 3)
        for i in range(0,3) : 
            _str = ' '
            _str2= ' ' 
            _str3 = ' '
            _str = _change(_replaceValuex(value , self._var1)[i] ) 
            _str2 = _change(_replaceValuex(value , self._var2)[i])
            _str3 = _change(_replaceValuex(value , self._var3)[i]) 
            self.a = self.a.astype(float)
            self.a[0][i] = (eval(_str))
            self.a[1][i] = (eval(_str2))
            self.a[2][i] = (eval(_str3))
        for i in range(0,3) : 
           for j in range(0,3) : 
               if i != j : 
                  b = (float(self.a[i][j]) + float(self.a[j][i]))/2
                  self.a[i][j] = self.a[j][i] = float(b) 
        self._label1 = Label(self  , text = 't11 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label1.grid(row = 10 , column =0)
        self._label2 = Label(self  , text = 't12 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label2.grid(row = 10 , column =2)
        self._Varlabel1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel1['text'] =  self.a[0][0]
        self._Varlabel1.grid(row = 10 , column =1)
        self._Varlabel2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE) 
        self._Varlabel2.grid(row = 10 , column =3)
        self._Varlabel2['text'] = self.a[0][1]
        self._label3 = Label(self  , text = 't13 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label3.grid(row = 10 , column =4)
        self._Varlabel3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel3['text'] = self.a[0][2]
        self._Varlabel3.grid(row = 10 , column =5) 
        self._label4 = Label(self  , text = 't21 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label4.grid(row = 11 , column =0 )
        self._Varlabel4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel4['text'] = self.a[0][1]
        self._Varlabel4.grid(row = 11 , column = 1 ) 
        self._label5 = Label(self  , text = 't22 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label5.grid(row = 11 , column =2 )
        self._Varlabel5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel5['text'] =  self.a[1][1]
        self._Varlabel5.grid(row = 11 , column = 3 ) 
        self._label6 = Label(self  , text = 't23 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label6.grid(row = 11 , column =4 )
        self._Varlabel6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel6['text'] =self.a[1][2]
        self._Varlabel6.grid(row = 11 , column = 5 ) 
        self._label7 = Label(self  , text = 't31 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label7.grid(row = 12 , column = 0 )
        self._Varlabel7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel7['text'] =self.a[0][2]
        self._Varlabel7.grid(row = 12 , column = 1 ) 
        self._label8 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label8.grid(row = 12 , column = 2 )
        self._Varlabel8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel8['text'] =self.a[1][2]
        self._Varlabel8.grid(row = 12 , column = 3 ) 
        self._label9 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label9.grid(row = 12 , column = 4 )
        self._Varlabel9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel9['text'] = self.a[2][2]
        self._Varlabel9.grid(row = 12 , column = 5 ) 
        self.button2 = Button(self ,text ='Tính Ứng suất ' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda : self._changepage())
        self.button2.grid(row = 13 , column = 3 )
        username = self.a 
    def _changepage(self) :  
        global username 
        self.master._v1 =  username
        #print(self.master._v1)
        self.master.switch_frame(tensorinput)  
class tensorinput(Frame): 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        super().__init__(*args, **kwargs) 
        Frame.config(self , bg = 'white' , width = 100)  
        global usernumber
        global condition
        self.a = self.master._v1  
        self._label1 = Label(self  , text = 't11 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label1.grid(row = 1 , column =0, padx = 3 , pady = 5)
        self._label2 = Label(self  , text = 't12 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label2.grid(row = 1 , column =2, padx = 3 , pady = 5)
        self._Varlabel1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel1['text'] =  self.a[0][0]
        self._Varlabel1.grid(row = 1 , column =1, padx = 3 , pady = 5)
        self._Varlabel2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE) 
        self._Varlabel2.grid(row = 1 , column =3, padx = 3 , pady = 5)
        self._Varlabel2['text'] = self.a[0][1]
        self._label3 = Label(self  , text = 't13 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label3.grid(row = 1 , column =4, padx = 3 , pady = 5)
        self._Varlabel3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel3['text'] = self.a[0][2]
        self._Varlabel3.grid(row = 1 , column =5, padx = 3 , pady = 5) 
        self._label4 = Label(self  , text = 't21 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label4.grid(row = 2 , column =0, padx = 3 , pady = 5 )
        self._Varlabel4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel4['text'] = self.a[0][1]

        self._Varlabel4.grid(row = 2 , column = 1 , padx = 3 , pady = 5) 
        self._label5 = Label(self  , text = 't22 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label5.grid(row = 2 , column =2  , padx = 3 , pady = 5 )
        self._Varlabel5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel5['text'] =  self.a[1][1]
        self._Varlabel5.grid(row = 2 , column = 3 , padx = 3 , pady = 5) 
        self._label6 = Label(self  , text = 't23 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label6.grid(row = 2 , column =4, padx = 3 , pady = 5 )
        self._Varlabel6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel6['text'] =self.a[1][2]
        self._Varlabel6.grid(row =2 , column = 5, padx = 3 , pady = 10 ) 
        self._label7 = Label(self  , text = 't31 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label7.grid(row = 3 , column = 0, padx = 3 , pady = 10 )
        self._Varlabel7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel7['text'] =self.a[0][2]
        self._Varlabel7.grid(row = 3 , column = 1, padx = 3 , pady = 10 ) 
        self._label8 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label8.grid(row = 3 , column = 2, padx = 3 , pady = 10 )
        self._Varlabel8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel8['text'] =self.a[1][2]
        self._Varlabel8.grid(row = 3 , column = 3, padx = 3 , pady = 10 ) 
        self._label9 = Label(self  , text = 't32 =' , font = ('Symbol' , 13 , 'bold' , 'italic') ,bg = 'White') 
        self._label9.grid(row = 3 , column = 4, padx = 3 , pady = 10)
        self._Varlabel9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)  
        self._Varlabel9['text'] = self.a[2][2]
        self._Varlabel9.grid(row = 3 , column = 5 , padx = 3 , pady = 10  ) 
        self.button2 = Button(self ,text ='Back' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda : master.switch_frame(Derapp))
        self.button2.grid(row = 0 , column = 0 , padx = 3 , pady = 5)
        self.lable1 = Label(self ,text = 'l = ' , font = ('Symbol' , 12 , 'bold' , 'italic') , relief = GROOVE ) 
        self.entry1 = Entry(self, relief = GROOVE ,bg = 'lavender')
        self.entry1.grid(row = 8 , column = 1 ) 
        self.lable1 .grid(row= 8 , column = 0 ) 
        self.label2 = Label(self , text = 'm = ' , font = ('Symbol' , 12 ,'bold' , 'italic' ), relief = GROOVE ) 
        self.entry2 = Entry(self , bg = 'lavender')  
        self.label2.grid(row = 8   , column = 2 ) 
        self.entry2.grid(row = 8 , column = 3 ) 
        #condition = self._k
        self._Button = Button(self , text = 'tính ứng suất' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE , command = lambda: self._func())
        self._Button.grid(row = 9 , column = 2 )
        usernumber = self.a 
        k1 = self.entry1.get() 
        k2 = self.entry2.get()
    def _func(self) : 
        global usernumber
        global condition
        _k1 = self.entry1.get() 
        _k2 = self.entry2.get()
        self.master.k1 = _k1 
        self.master.k2 = _k2
        self.arrval =usernumber
        self._v = self.arrval[0][0] + self.arrval[1][1] + self.arrval[2][2]
        self.a = np.arange(9).reshape(3, 3) 
        self.theta = [[1,0,0],[0,1,0],[0,0,1]] 
        self.a = self.a.astype(float) 
        for i in range(0,3) : 
            for j in range (0,3) : 
             self.a[i][j] = eval(self.master.k1)*self._v*self.theta[i][j] + 2*eval(self.master.k2)*self.arrval[i][j] 
        condition = self.a 
        self.master.var1 = condition
        self.master.var2 = 1 
        self.master.switch_frame(Page1_Frame2)
        print(self.master.var1)
class Page1_frame(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.label2 = Label(self, text="Tính Tensor Ứng suất 3D(2D)", font=('Times', 15, 'bold'),bg = 'blue3' , fg = 'white')
        self.label1 = Label(self, text="Nhập vào ma trận ứng suất", font=('Helvetica', 10, 'italic' ,'bold'))
        self.label2.grid(rows=1, column=1)
        self.label1.grid(rows=2, column=1)
        self.entry1 = Entry(self, bd=2, width=20 , textvariable = '1')
        self.entry1.grid(row=4, column=0, padx=5, pady=10)
        self.entry2 = Entry(self, bd=2, width=20 ,textvariable = '2' )
        self.entry2.grid(row=4, column=1, padx=5, pady=10)
        self.entry3 = Entry(self, bd=2, width=20 , textvariable = '3')
        self.entry3.grid(row=4, column=2, padx=5, pady=10)
        self.entry4 = Entry(self, bd=2, width=20 , textvariable = '2')
       
        self.entry4.grid(row=5, column=0, padx=5, pady=10)
        self.entry5 = Entry(self, bd=2, width=20 ,textvariable = '5')
        self.entry5.grid(row=5, column=1, padx=5, pady=10)
        self.entry6 = Entry(self, bd=2, width=20,textvariable = '6')
        self.entry6.grid(row=5, column=2, padx=5, pady=10)
        self.entry7 = Entry(self, bd=2, width=20,textvariable = '3')
       
        self.entry7.grid(row=6, column=0, padx=5, pady=10)
        self.entry8 = Entry(self, bd=2, width=20,textvariable = '6')
     
        self.entry8.grid(row=6, column=1, padx=5, pady=10 )
        self.entry9 = Entry(self, bd=2, width=20, textvariable = '9')
        self.entry9.grid(row=6, column=2, padx=5, pady=10)
        self.BUTTONCAL = Button(self, text=" Tính các chỉ số ma trận", font =('calibri' , 10 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.switch_frame)
        self.BUTtoncal = Button(self, text=" tính các chỉ số ma trận với góc alpha ", font =('calibri' , 10 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.switch_frame2)
        self.ButtonBack = Button(self , text ='<-------' , font =('calibri' , 10 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command = lambda : master.switch_frame(MainApp)) 
        self.ButtonBack.grid(row=11, column=1)
        self.BUTtoncal.grid(row = 10 , column = 1)
        var1 = self.entry1.get()
        var2 = self.entry2.get()
        var3 = self.entry3.get()
        var4 = self.entry2.get()
        var5 = self.entry5.get()
        var6 = self.entry6.get()
        var7 = self.entry3.get()
        var8 = self.entry6.get()
        var9 = self.entry9.get()
        self.BUTTONCAL.grid(row=7, column=1)  
  
    def switch_frame(self):
        _var1 = self.entry1.get()
        _var2 = self.entry2.get()
        _var3 = self.entry3.get()
        _var4 = self.entry2.get()
        _var5 = self.entry5.get()
        _var6 = self.entry6.get()
        _var7 = self.entry3.get()
        _var8 = self.entry6.get()
        _var9 = self.entry9.get()
        self.master.var1 = [[_var1,_var2,_var3],[_var4,_var5,_var6],[_var7,_var8,_var9]]
        self.master.var2 = 0 
        self.master.switch_frame(Page1_Frame2)
    def switch_frame2(self):
        _var1 = self.entry1.get()
        _var2 = self.entry2.get()
        _var3 = self.entry3.get()
        _var4 = self.entry2.get()
        _var5 = self.entry5.get()
        _var6 = self.entry6.get()
        _var7 = self.entry3.get()
        _var8 = self.entry6.get()
        _var9 = self.entry9.get()
        self.master.var1 = _var1
        self.master.var2 = _var2
        self.master.var3 = _var3
        self.master.var4 = _var4
        self.master.var5 = _var5
        self.master.var6 = _var6
        self.master.var7 = _var7
        self.master.var8 = _var8
        self.master.var9 = _var9
        self.master.var1 = [[_var1,_var2,_var3],[_var4,_var5,_var6],[_var7,_var8,_var9]]
        self.master.switch_frame(Page1_frame4) 
class Page1_Frame2(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Frame.__init__(self, master, *args, **kwargs) 
        Frame.config(self , bg = 'white' , width = 100)
        a = np.arange(9).reshape(3, 3)
        self.label = Label(self, text='Ma Trận ứng suất tương ứng', font=('Times', 13, 'bold') ,fg = 'white' , bg = 'blue2')
        self.label.grid(row=0, column=1, pady=5, padx=5)
        self.var1 = float(self.master.var1[0][0])
        self.var2 = float(self.master.var1[0][1])
        self.var3 = float(self.master.var1[0][2])
        self.var4 = float(self.master.var1[1][0])
        self.var5 = float(self.master.var1[1][1])
        self.var6 = float(self.master.var1[1][2])
        self.var7 = float(self.master.var1[2][0])
        self.var8 = float(self.master.var1[2][1])
        self.var9 = float(self.master.var1[2][2])
        self.varcount = self.master.var2
        self.label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label1.grid(row=1, column=0)
        self.label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label2.grid(row=1, column=1)
        self.label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label3.grid(row=1, column=2)
        self.label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label4.grid(row=2, column=0)
        self.label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label5.grid(row=2, column=1)
        self.label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label6.grid(row=2, column=2)
        self.label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label7.grid(row=3, column=0)
        self.label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label8.grid(row=3, column=1)
        self.label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label9.grid(row=3, column=2)
        self.label1['text'] = self.var1
        self.label2['text'] = self.var2
        self.label3['text'] = self.var3
        self.label4['text'] = self.var4
        self.label5['text'] = self.var5
        self.label6['text'] = self.var6
        self.label7['text'] = self.var7
        self.label8['text'] = self.var8
        self.label9['text'] = self.var9
        a = [[self.var1, self.var2, self.var3], [self.var4, self.var5, self.var6], [self.var7, self.var8, self.var9]]
        V, D = np.linalg.eig(a)
        self.__var1 = V[0]
        self.__var2 = V[1]
        self.__var3 = V[2]
        self._label = Label(self, text="Ứng Suất chính", font=('Times', 14, 'bold') , bg = 'blue3' , fg = 'white')
        self._label.grid(row=4, column=1)
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=0)
        self._label1['text'] ='\u03B5 ' +"1"+ " = " + str(V[0])
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=1)
        self._label1['text'] ='\u03B5 ' +"2"+ " = " + str(self.__var2)
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=2)
        self._label1['text'] = '\u03B5 ' +"3"+ " = " + str(self.__var3)
        self.__llabel2 = Label(self, text="Phương chính",font=('Times', 14, 'bold') , bg = 'blue3' , fg = 'white')
        self.__llabel2.grid(row=6, column=1)
        self.__label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label1.grid(row=7, column=0)
        self.__label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label2.grid(row=7, column=1)
        self.__label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label3.grid(row=7, column=2)
        self.__label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label4.grid(row=8, column=0)
        self.__label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label5.grid(row=8, column=1)
        self.__label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label6.grid(row=8, column=2)
        self.__label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label7.grid(row=9, column=0)
        self.__label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label8.grid(row=9, column=1)
        self.__label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label9.grid(row=9, column=2)
        self.__label1['text'] = "l1 = " + str(D[0][0])
        self.__label2['text'] = "l2 = " + str(D[0][1])
        self.__label3['text'] = "l3 = " + str(D[0][2])
        self.__label4['text'] = "m1 = " + str(D[1][0])
        self.__label5['text'] = "m2 = " + str(D[1][1])
        self.__label6['text'] = "m3 = " + str(D[1][2])
        self.__label7['text'] = "n1 = " + str(D[2][0])
        self.__label8['text'] = "n2 = " + str(D[2][1])
        self.__label9['text'] = "n3 = " + str(D[2][2])
        if self.varcount == 1 : 
            self.button = Button(self, text='BACK',font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=lambda: master.switch_frame(tensorinput))
            self.button2 = Button(self , text = 'Tính ứng suất nghiêng tương ứng' ,font =('calibri' , 9 , 'bold'),  bg = 'ivory3', command = lambda : master.switch_frame(Page1_frame4))
            self.button.grid(row=10, column=1)
            self.button2.grid(row = 11 , column =1 )
        else : 
            self.button = Button(self, text='BACK',font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=lambda: master.switch_frame(Page1_frame))
            self.button2 = Button(self , text = 'Tính ứng suất nghiêng tương ứng' ,font =('calibri' , 9 , 'bold'),  bg = 'ivory3', command = lambda : master.switch_frame(Page1_frame4))
            self.button2.grid(row = 10 , column =1 )
            self.button.grid(row=11, column=1)
        if(a[0][2] == 0 and a[1][2] == 0 and a[2][2] ==  0 and a[2][1] == 0 and a[2][0] == 0 ) :
            self.button2Val = Button(self , text = 'DRAW 2D ' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE  , command = self.draw2d)
            self.button2Val.grid(row = 10 , column = 2)
        else :
            self.button2Val = Button(self, text='DRAW 3D ', font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.draw3d)
            self.button2Val.grid(row=10, column=2)
    def draw2d(self):
        self.z = np.linspace(0, 360, 360)
        self.r = np.sqrt(((self.var5 - self.var1) / 2) ** 2 + self.var2 ** 2)
        self.x = (self.var5+ self.var1) / 2 + self.r * np.cos(np.radians(self.z))
        self.y = self.r * np.sin(np.radians(self.z))
        self.a = ([self.var1, self.var1, self.var5, self.var5, self.var1])
        self.b = ([0,self.var2, -self.var2, 0, 0])
        mlp.plot(self.a, self.b, self.x, self.y)
        mlp.xlabel(r"$\sigma$", size=18)
        mlp.ylabel(r"$\tau$", size=18)
        mlp.axis('equal')
        mlp.grid()
        mlp.show()
    def draw3d(self):
        a = [[self.var1, self.var2, self.var3], [self.var4, self.var5, self.var6], [self.var7, self.var8, self.var9]]
        M3 , M2 , M1 = np.linalg.eigvalsh(a)
        self.R_max = 0.5*(M1-M3)
        self.cent_max = 0.5*(M1 + M3)
        self.R_min = 0.5*(M2-M3)
        self.cent_min = 0.5*(M2 + M3)
        self.R_mid = 0.5*(M1 - M2)
        self.cent_mid = 0.5*(M1 + M2)
        circle1 = mlp.Circle((self.cent_max, 0), self.R_max, facecolor='#cce885', lw=3, edgecolor='#5c8037')
        circle2 = mlp.Circle((self.cent_min, 0), self.R_min, facecolor='w', lw=3, edgecolor='#15a1bd')
        circle3 = mlp.Circle((self.cent_mid, 0), self.R_mid, facecolor='w', lw=3, edgecolor='#e4612d')
        mlp.axis('image')
        ax = mlp.gca()
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(circle3)
        ax.set_xlim(M3 - .1 * self.R_max, M1 + .1 * self.R_max)
        ax.set_ylim(-1.1 * self.R_max, 1.1 * self.R_max)
        mlp.xlabel(r"$\sigma$", size=18)
        mlp.ylabel(r"$\tau$", size=18)
        mlp.savefig('Mohr_circle_3D.svg')
        mlp.grid()
        mlp.show()

class Page1_frame4(Frame):
    def __init__(self, master, *args, **kwargs):
        #super().__init__( *args, **kwargs  )
        Frame.__init__(self, master, *args, **kwargs)
        global _var1
        self.label = Label(self, text='Ma Trận ứng suất tương ứng', font=('Times', 13, 'bold') ,fg = 'white' , bg = 'blue2')
        self.label.grid(row=0, column=1, pady=5, padx=5)
        self.var1 = float(self.master.var1[0][0])
        self.var2 = float(self.master.var1[0][1])
        self.var3 = float(self.master.var1[0][2])
        self.var4 = float(self.master.var1[1][0])
        self.var5 = float(self.master.var1[1][1])
        self.var6 = float(self.master.var1[1][2])
        self.var7 = float(self.master.var1[2][0])
        self.var8 = float(self.master.var1[2][1])
        self.var9 = float(self.master.var1[2][2])
        self.label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label1.grid(row=1, column=0)
        self.label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label2.grid(row=1, column=1)
        self.label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label3.grid(row=1, column=2)
        self.label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label4.grid(row=2, column=0)
        self.label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label5.grid(row=2, column=1)
        self.label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label6.grid(row=2, column=2)
        self.label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label7.grid(row=3, column=0)
        self.label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label8.grid(row=3, column=1)
        self.label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label9.grid(row=3, column=2)
        self.label1['text'] = self.var1
        self.label2['text'] = self.var2
        self.label3['text'] = self.var3
        self.label4['text'] = self.var4
        self.label5['text'] = self.var5
        self.label6['text'] = self.var6
        self.label7['text'] = self.var7
        self.label8['text'] = self.var8
        self.label9['text'] = self.var9
        self.entry = Entry(self , textvariable = '__')
        self.entry.grid(row=4, column=1)
        self.label = Label(self, text= 'enter \u03C6 ' , font = ('Times' , 12 , 'bold' ) ,bg = 'White') 
        self.label.grid(row=4, column=0)
        _var1 = self.entry.get() 
        self.comboboxLabel = Label(self , text =  'chọn chế độ \u03C6 ')  
        self.n  = StringVar()
        self.combox = ttk.Combobox(self , width = 12 , textvariable =self.n) 
        self.combox['values'] = ('Dec' , 'Rad')  
        self.combox.grid(row = 4 , column =2  )   
        self.combox.current(0)
        comboxget = self.combox.get()  
        #self._label = Label(self , text = 'in DEC mode' , font = ('Times' , 12 , 'bold' ) ,bg = 'White') 
        #self._label.grid(row = 4  , column =2 )
        self.button2 = Button(self, text='CALCULATED',  font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , command=self.switch_frame1)
        self.button2.grid(row=5, column=1)
        self.button3 = Button(self , text='Back',  font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , command=lambda : master.switch_frame(Page1_frame)) 
        self.button3.grid(row =6 , column = 1 )
    def switch_frame1(self):
        __var1 = self.entry.get() 
        varget = self.combox.get()
        self.master._var1 = __var1 
        self.master.comboxget = varget 
        if((self.entry.get()) == '') :
            try : 
                float(self.entry.get() )
            except ValueError : 
                self.msg = messagebox.askquestion("" , "bạn có muốn nhập lại ")
                if self.msg =='yes' : 
                    self.master.switch_frame(Page1_frame4)
                elif self.msg  == 'No' : 
                    exit()
        else : 
            self.master.switch_frame(Page1_Frame5)       
class Page1_Frame5(Frame):
    def __init__(self, master, *args, **kwargs):
        #super().__init__(   )
        Frame.__init__(self, master, *args, **kwargs)
        a = np.arange(9).reshape(3, 3)
        self.systemalpha = self.master.comboxget 
        self.var1 = float(self.master.var1[0][0])
        self.var2 = float(self.master.var1[0][1])
        self.var3 = float(self.master.var1[0][2])
        self.var4 = float(self.master.var1[1][0])
        self.var5 = float(self.master.var1[1][1])
        self.var6 = float(self.master.var1[1][2])
        self.var7 = float(self.master.var1[2][0])
        self.var8 = float(self.master.var1[2][1])
        self.var9 = float(self.master.var1[2][2])
        self._var = float(self.master._var1)
        if self.systemalpha == 'Rad' : 
            pass 
        elif (self.systemalpha == 'Dec'):
            self._var = (self._var*mth.pi)/180 
        a = [[self.var1, self.var2, self.var3], [self.var4, self.var5, self.var6], [self.var7, self.var8, self.var9]]
        self.lable = Label(self, text="Ma trận",font=('Times', 13, 'bold') ,fg = 'white' , bg = 'blue2')
        self.lable.grid(row=0, column=1, pady=5)
        self.uxx = (a[0][0] + a[1][1])*0.5+ (a[0][0] - a[1][1]) * mth.cos(2 * self._var) * 0.5 + a[0][1] * mth.sin(
            2 * self._var)
        self.uxy = -(a[0][0] - a[1][1]) * mth.sin(2 * self._var) * 0.5 + a[0][1] * mth.cos(2 * self._var)
        self.uyy = (a[0][0] + a[1][1]) *0.5 - (a[0][0] - a[1][1]) * mth.cos(2 * self._var) * 0.5 + a[0][1] * mth.sin(
            2 * self._var)
        self.label1 = Label(self)
        self.label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label1.grid(row=2, column=0)
        self.label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label2.grid(row=2, column=1)
        self.label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label3.grid(row=2, column=2)
        self.label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label4.grid(row=3, column=0)
        self.label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label5.grid(row=3, column=1)
        self.label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label6.grid(row=3, column=2)
        self.label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label7.grid(row=4, column=0)
        self.label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label8.grid(row=4, column=1)
        self.label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label9.grid(row=4, column=2,  pady=5, padx = 1 )
        self.label1['text'] = "\u03B5'11 = " + str(self.uxx)
        self.label2['text'] = "\u03B5'12 = " + str(self.uxy)
        self.label3['text'] = "\u03B5'21 = " + str(self.uxy)
        self.label4['text'] = "\u03B5'22 = " + str(self.uyy)
        self.label5['text'] = "\u03B5'13 = " + str(0)
        self.label6['text'] = "\u03B5'23 = " + str(0)
        self.label7['text'] = "\u03B5'31 = " + str(0)
        self.label8['text'] = "\u03B5'32 = " + str(0)
        self.label9['text'] = "\u03B5'33 = " + str(1)
        self.label10 = Label(self, font=('Time', 12, 'bold')) 
        
        self.label10['text'] = '\u03C6' + "= " + str(self._var) + " (rad) "
        self.label10.grid(row=1, column=1)
        self.button1 = Button(self, text='trở lại ma trận trước ', font =('calibri' , 9 , 'bold'),  bg = 'ivory3', command=lambda: master.switch_frame(Page1_frame))
        self.button1.grid(row=9, column=1, pady=5)
        self.button1_ =   Button(self, text='<------', font =('calibri' , 9 , 'bold'),  bg = 'ivory3', command=lambda: master.switch_frame(Page1_frame4))
        self.button1_.grid(row=10, column=1)
       
class Page1_Frame6(Frame) : 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        Frame.config(self , bg = 'white' , width = 100)
        super().__init__(*args, **kwargs)
        self.label2 = Label(self, text="Tính Biến dạng 3D(2D)", font=('Times', 15, 'bold'),bg = 'blue3' , fg = 'white')
        self.label1 = Label(self, text="Nhập vào ma trận biến dạng ", font=('Helvetica', 10, 'italic' ,'bold'))
        self.label2.grid(rows=1, column=1)
        self.label1.grid(rows=2, column=1)
        self.entry1 = Entry(self, bd=2, width=20 , textvariable = '_1')
        self.entry1.grid(row=4, column=0, padx=5, pady=10)
        self.entry2 = Entry(self, bd=2, width=20 ,textvariable = '_2' )
        self.entry2.grid(row=4, column=1, padx=5, pady=10)
        self.entry3 = Entry(self, bd=2, width=20 , textvariable = '_3')
        self.entry3.grid(row=4, column=2, padx=5, pady=10)
        self.entry4 = Entry(self, bd=2, width=20 , textvariable = '_2')
       
        self.entry4.grid(row=5, column=0, padx=5, pady=10)
        self.entry5 = Entry(self, bd=2, width=20 ,textvariable = '_5')
        self.entry5.grid(row=5, column=1, padx=5, pady=10)
        self.entry6 = Entry(self, bd=2, width=20,textvariable = '_6')
        self.entry6.grid(row=5, column=2, padx=5, pady=10)
        self.entry7 = Entry(self, bd=2, width=20,textvariable = '_3')
       
        self.entry7.grid(row=6, column=0, padx=5, pady=10)
        self.entry8 = Entry(self, bd=2, width=20,textvariable = '_6')
     
        self.entry8.grid(row=6, column=1, padx=5, pady=10 )
        self.entry9 = Entry(self, bd=2, width=20, textvariable = '_9')
        self.entry9.grid(row=6, column=2, padx=5, pady=10)
        self.BUTTONCAL = Button(self, text=" CALULATED ", font =('calibri' , 10 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.switch_frame)
        self.BUTtoncal = Button(self, text=" CALULATED tensor with alpha ", font =('calibri' , 12 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.switch_frame)
        self.ButtonBack = Button(self , text ='<-------' , font =('calibri' , 10 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command = lambda : master.switch_frame(MainApp)) 
        self.ButtonBack.grid(row=9, column=1)
        var1 = self.entry1.get()
        var2 = self.entry2.get()
        var3 = self.entry3.get()
        var4 = self.entry2.get()
        var5 = self.entry5.get()
        var6 = self.entry6.get()
        var7 = self.entry3.get()
        var8 = self.entry6.get()
        var9 = self.entry9.get()
        self.BUTTONCAL.grid(row=7, column=1)  
    def switch_frame(self):
        _var1 = self.entry1.get()
        _var2 = self.entry2.get()
        _var3 = self.entry3.get()
        _var4 = self.entry2.get()
        _var5 = self.entry5.get()
        _var6 = self.entry6.get()
        _var7 = self.entry3.get()
        _var8 = self.entry6.get()
        _var9 = self.entry9.get()
        self.master.var1 = [[_var1,_var2,_var3],[_var4,_var5,_var6],[_var7,_var8,_var9]]
        self.master.var2 = 0 
        self.master.switch_frame(Page1_Frame7)
class Page1_Frame7(Frame) : 
     def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Frame.__init__(self, master, *args, **kwargs) 
        Frame.config(self , bg = 'white' , width = 100)
        a = np.arange(9).reshape(3, 3)
        self.label = Label(self, text='Ma Trận Biến dạng tương ứng', font=('Times', 13, 'bold') ,fg = 'white' , bg = 'blue2')
        self.label.grid(row=0, column=1, pady=5, padx=5)
        self.var1 = float(self.master.var1[0][0])
        self.var2 = float(self.master.var1[0][1])
        self.var3 = float(self.master.var1[0][2])
        self.var4 = float(self.master.var1[1][0])
        self.var5 = float(self.master.var1[1][1])
        self.var6 = float(self.master.var1[1][2])
        self.var7 = float(self.master.var1[2][0])
        self.var8 = float(self.master.var1[2][1])
        self.var9 = float(self.master.var1[2][2])
        self.varcount = self.master.var2
        self.label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label1.grid(row=1, column=0)
        self.label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label2.grid(row=1, column=1)
        self.label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label3.grid(row=1, column=2)
        self.label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label4.grid(row=2, column=0)
        self.label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label5.grid(row=2, column=1)
        self.label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label6.grid(row=2, column=2)
        self.label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label7.grid(row=3, column=0)
        self.label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label8.grid(row=3, column=1)
        self.label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.label9.grid(row=3, column=2)
        self.label1['text'] = self.var1
        self.label2['text'] = self.var2
        self.label3['text'] = self.var3
        self.label4['text'] = self.var4
        self.label5['text'] = self.var5
        self.label6['text'] = self.var6
        self.label7['text'] = self.var7
        self.label8['text'] = self.var8
        self.label9['text'] = self.var9
        a = [[self.var1, self.var2, self.var3], [self.var4, self.var5, self.var6], [self.var7, self.var8, self.var9]]
        V, D = np.linalg.eig(a)
        self.__var1 = V[0]
        self.__var2 = V[1]
        self.__var3 = V[2]
        self._label = Label(self, text="Biến Dạng chính", font=('Times', 14, 'bold') , bg = 'blue3' , fg = 'white')
        self._label.grid(row=4, column=1)
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=0)
        self._label1['text'] ='\u03B5 ' +"1"+ " = " + str(V[0])
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=1)
        self._label1['text'] ='\u03B5 ' +"2"+ " = " + str(self.__var2)
        self._label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self._label1.grid(row=5, column=2)
        self._label1['text'] = '\u03B5 ' +"3"+ " = " + str(self.__var3)
        self.__llabel2 = Label(self, text="Phương chính",font=('Times', 14, 'bold') , bg = 'blue3' , fg = 'white')
        self.__llabel2.grid(row=6, column=1)
        self.__label1 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label1.grid(row=7, column=0)
        self.__label2 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label2.grid(row=7, column=1)
        self.__label3 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label3.grid(row=7, column=2)
        self.__label4 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label4.grid(row=8, column=0)
        self.__label5 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label5.grid(row=8, column=1)
        self.__label6 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label6.grid(row=8, column=2)
        self.__label7 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label7.grid(row=9, column=0)
        self.__label8 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label8.grid(row=9, column=1)
        self.__label9 = Label(self  , font = ('Times' , 12 , 'bold' ) ,bg = 'White' , relief = GROOVE)
        self.__label9.grid(row=9, column=2)
        self.__label1['text'] = "l1 = " + str(D[0][0])
        self.__label2['text'] = "l2 = " + str(D[0][1])
        self.__label3['text'] = "l3 = " + str(D[0][2])
        self.__label4['text'] = "m1 = " + str(D[1][0])
        self.__label5['text'] = "m2 = " + str(D[1][1])
        self.__label6['text'] = "m3 = " + str(D[1][2])
        self.__label7['text'] = "n1 = " + str(D[2][0])
        self.__label8['text'] = "n2 = " + str(D[2][1])
        self.__label9['text'] = "n3 = " + str(D[2][2])
        if self.varcount == 1 : 
            self.button = Button(self, text='BACK',font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=lambda: master.switch_frame(tensorinput))
            # self.button2 = Button(self , text = 'cal' , command = lambda : master.switch_frame(Page1_frame3))
            self.button.grid(row=10, column=1)
            # self.button2.grid(row = 10 , column =2 )
        else : 
            self.button = Button(self, text='BACK',font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=lambda: master.switch_frame(Page1_Frame6))
            self.button.grid(row=10, column=1)
        if(a[0][2] == 0 and a[1][2] == 0 and a[2][2] ==  0 and a[2][1] == 0 and a[2][0] == 0 ) :
            self.button2Val = Button(self , text = 'DRAW 2D ' , font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE  , command = self.draw2d)
            self.button2Val.grid(row = 10 , column = 2)
        else :
            self.button2Val = Button(self, text='DRAW 3D ', font =('calibri' , 9 , 'bold'),  bg = 'ivory3' , relief = GROOVE, command=self.draw3d)
            self.button2Val.grid(row=10, column=2)
     def draw3d(self):
            a = [[self.var1, self.var2, self.var3], [self.var4, self.var5, self.var6], [self.var7, self.var8, self.var9]]
            M3 , M2 , M1 = np.linalg.eigvalsh(a)
            self.R_max = 0.5*(M1-M3)
            self.cent_max = 0.5*(M1 + M3)
            self.R_min = 0.5*(M2-M3)
            self.cent_min = 0.5*(M2 + M3)
            self.R_mid = 0.5*(M1 - M2)
            self.cent_mid = 0.5*(M1 + M2)
            circle1 = mlp.Circle((self.cent_max, 0), self.R_max, facecolor='#cce885', lw=3, edgecolor='#5c8037')
            circle2 = mlp.Circle((self.cent_min, 0), self.R_min, facecolor='w', lw=3, edgecolor='#15a1bd')
            circle3 = mlp.Circle((self.cent_mid, 0), self.R_mid, facecolor='w', lw=3, edgecolor='#e4612d')
            mlp.axis('image')
            ax = mlp.gca()
            ax.add_artist(circle1)
            ax.add_artist(circle2)
            ax.add_artist(circle3)
            ax.set_xlim(M3 - .1 * self.R_max, M1 + .1 * self.R_max)
            ax.set_ylim(-1.1 * self.R_max, 1.1 * self.R_max)
            mlp.xlabel(r"$\sigma$", size=18)
            mlp.ylabel(r"$\tau$", size=18)
            mlp.savefig('Mohr_circle_3D.svg')
            mlp.grid()
            mlp.show()
     def draw2d(self):
            self.z = np.linspace(0, 360, 360)
            self.r = np.sqrt(((self.var5 - self.var1) / 2) ** 2 + self.var2 ** 2)
            self.x = (self.var5+ self.var1) / 2 + self.r * np.cos(np.radians(self.z))
            self.y = self.r * np.sin(np.radians(self.z))
            self.a = ([self.var1, self.var1, self.var5, self.var5, self.var1])
            self.b = ([0,self.var2, -self.var2, 0, 0])
            mlp.plot(self.a, self.b, self.x, self.y)
            mlp.xlabel(r"$\sigma$", size=18)
            mlp.ylabel(r"$\tau$", size=18)
            mlp.axis('equal')
            mlp.grid()
            mlp.show()
    
if __name__ == "__main__":

   Rootapp = rootapp()
   Rootapp.mainloop() 
   #command("D=123;L=123;") 

   """_s = ZIgmachange('x*y+x^2+y^2+z^2') 
   s= _Dervaluex('x*y+x**2+y**2')
   value = ['1' ,'2','3']
   print(_s)
   print(_replaceValuex(value ,'x*y' ))"""
  # print(_Dervaluex('x**3+y**3'))