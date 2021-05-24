from collections import deque 
import math
class Case(Exception) : 
    pass 
class SingleFatNode(Case) : 
    pass   
class MiddleRigid(Case) : 
    pass 
class Allrigid(Case) : 
    pass 
def token(s) : 
    _char = [] 
    _crash = [] 
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = "" 
    for i in alphabet : 
        _str += i  
    _str = _str + "-0123456789"+_str.upper()+"*/+-^()->."
    while(s) : 
        if s[0] in _str : 
            TakeNumber = s[0] 
            s = s[1:] 
            while(s and s[0] in _str)  : 
                TakeNumber += s[0] 
                s = s[1:] 
            _char.append(TakeNumber) 
            if s : 
                _crash.append(s[0]) 
                s = s[1:] 
        else : 
            _char.append(s[0]) 
            s = s[1:] 
    return _char    
def mergeNumber(s) : 
    _char = [] 
    _crash = [] 
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = "" 
    for i in alphabet : 
        _str += i  
    _str = _str + "-0123456789"+_str.upper()+"*/+^.>"
    while(s) : 
        if s[0] in _str : 
            TakeNumber = s[0] 
            s = s[1:] 
            while(s and s[0] in _str)  : 
                TakeNumber += s[0] 
                s = s[1:] 
            _char.append(TakeNumber) 
            if s : 
                _crash.append(s[0]) 
                s = s[1:] 
        else : 
            _char.append(s[0]) 
            s = s[1:] 
    return _char     
def Mer2(s) : 
    _char = [] 
    _crash = [] 
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = "" 
    for i in alphabet : 
        _str += i  
    _str = _str + "0123456789"+_str.upper()+"*/+^.>"
    while(s) : 
        if s[0] in _str : 
            TakeNumber = s[0] 
            s = s[1:] 
            while(s and s[0] in _str)  : 
                TakeNumber += s[0] 
                s = s[1:] 
            _char.append(TakeNumber) 
            if s : 
                _crash.append(s[0]) 
                s = s[1:] 
        else : 
            _char.append(s[0]) 
            s = s[1:] 
    return _char     
def checchar(orient) :  
    for i in range (0,len(orient) ) :  
        for j in range(0 , len(orient[i])) : 
            if (not orient[i][j].isdigit() ) : 
                 return False 
    return True
def checkCharinString(_lst): 
    stack =  [] 
    pass
def getString(s) :  
    return token(s)  
def getNameofMaterial(arr , line_count ) : 
    ar = [] 
    Arr= []
    for i in range (len(arr))  : 
        ar.append(getString(arr[i])) 
    for i in range(line_count ) : 
        Arr.append(ar[i][0]) 
    return Arr 
def GetNameMaterialDICt(arr , line_count ) : 
    ar = [] 
    Arr = []  
    _dictOfdata = {} 
    for i in range(len(arr) ) :  
        ar.append(getString(arr[i])) 
    for i in range(line_count)  : 
         Arr.append(ar[i][0])      
         _dictOfdata.__setitem__(ar[i][0] , [ar[i][1] , ar[i][2],ar[i][3]]) 
    return _dictOfdata  
def splitsym(orient) :  
    lst = []
    for i in range (0,len(orient) ) :  
        for j in range(0 , len(orient[i])) : 
            if (not orient[i][j].isdigit())  : 
                if('.' not in orient[i][j]) :
                     lst.append(orient[i][j])       
    return lst   
def replaceVal(Llst , Dict ) : 
    arr=[]
    k =[]
    _arr = []
    _str = " "
    len_lst = len(Llst)
    for i in range (0,len_lst) : 
        k = split(Llst[i])
        for j in range(len(k) )  : 
            if(k[j].isalpha()) : 
                k[j] = Dict[k[j]]   
        _str = ""
        for j in range (len(k)) : 
            _str += k[j] 
        _arr.append(_str)
    for i in range (len(_arr)) : 
        _arr[i] = eval(_arr[i]) 
    return(_arr)
        
def slpittoStack(s) : 
    _stack = []
    for  i in s :  
        _stack.append(i) 
    return _stack 
def split(char1) : 
    return [char for char in char1] 
def search(arr , left , right  , value) : 
    if  right >= left  : 
        mid = left +(right - left)/2 
        if (arr[mid] == value ) : 
            return True
        elif (arr[mid] > value ) : 
            return search(arr ,left , mid-1, value ) 
        else : 
            return search(arr , mid+1 , right , value ) 
    else  : return -1 
def _charsym(_str) :  
    k =[]
    l = []
    temp = []
    str1 = '*/+-'
    for i in _str :  
        k.append(split(i))
    for i in k : 
        l = l+i  
    k.clear() 
    for i in l   : 
        if  (i.isdigit()) : 
            temp.append(i) 
        elif i in str1 : 
            temp.append(i)
    for i in temp : 
        l.remove(i)
    l = set(l) 
    for i in  l  : 
        k.append(i)
    return  k 
class function : 
    def __init__(self) : 
        self.key = 0  
        self.value = 0  
    def getindict(self , _str )   :  
        lst = token(_str) 
        pair = ()
        for i in range(0 , len(_str)) : 
            pair = (lst[0] , lst[1]) 
        return pair  
def checkNumber(s) :
    try : 
        float(s) 
        return True 
    except ValueError :  
        return False  
def declaration(s) :  
    pofix = [] 
    _stack = []
    Dict ={}  
    stack = []  
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = ""  
    for i in alphabet : 
        _str += i  
    _str = _str + "-0123456789"+_str.upper()+"*/+-^."  
    _str = _str.replace('O','')  
    _str = _str.replace('o','')
    count  = 0  
    pos = 0  
    if(len(s)!= 0) : 
        s = mergeNumber(s) 
        pos = len(s)
        i =0 
        j = 1 
        while(i < len(s) and j < len(s)) : 
            Dict.__setitem__(s[i] , s[j] )  
            i +=2
            j +=2 
    return  Dict
def splitText(s,pos) :  
    pofix = [] 
    stack  = []      
    count =  0 
    s = mergeNumber(s)  
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = ""  
    for i in alphabet : 
        _str += i  
    _str = _str + "-0123456789"+_str.upper()+"*/+^."
    for i in range(pos , len(s)) :   
        _tuple=()  
        _stack = [] 
        if(s[i] in _str or len(s[i])>1) : 
            stack.append(s[i]) 
        elif (s[i] == ';'or s[i] =='->') : 
            while(len(stack) != 0) : 
                 _stack.append(stack.pop())  
            pofix.append(_stack[::-1]) 
        elif (s[i] == '|') :  
            break 
        else : continue
    if (len(stack) != 0 )      : 
        while(len(stack) != 0) : 
            _stack.append(stack.pop())  
        pofix.append(_stack[::-1]) 
    for i in range (len(s)) : 
        if (s[i] =='|') : 
           pos  = i 
           break 
    return (pofix ,pos)
def _repval(s,_dict) : 
    lst = []
    for i in range(len(s)) :  
        for j in range(len(s[i])) : 
            _lst =[]
            if(s[i][j].isalpha() or len(s[i][j]) > 1 ) :   
                if(s[i][j] !='O') :
                    _lst.append([s[i][j]])    
                    s[i][j] = str(replaceVal(_lst[0],_dict)[0]) 
                else :  pass 
    return s     

def Momentcode(s,pos) : 
    pofix = [] 
    stack = []
    s = mergeNumber(s)  
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = ""   
    
    if('|' in s ) : 
        for i in alphabet :  
                _str += i  
        _str = _str + "-0123456789"+_str.upper()+"*/+-^."
        for i in range(pos+1 , len(s)) :   
            _tuple=()  
            _stack = [] 
            if(s[i] in _str or len(s[i])>1) : 
                stack.append(s[i]) 
            elif (s[i] == ';') : 
                while(len(stack) != 0) : 
                    _stack.append(stack.pop())  
                pofix.append(_stack[::-1])     
            elif (s[i] == '|') :  
                break         
            else : continue 
        if (len(stack) != 0 )      : 
            while(len(stack) != 0) : 
                _stack.append(stack.pop())  
            pofix.append(_stack[::-1])  
        for  j in range (pos+1 , len(s)) : 
            if(s[j] == '|') : 
                pos = j  
                break 
    return (pofix,pos  ) 
def gripcode(s , pos) :  
   pofix = [] 
   pofix = Momentcode(s,pos)[0] 
   return (pofix,Momentcode(s,pos)[1] )
def  Find(_dict,s )  :   
        lst = [] 
        k = list(_dict.keys()) 
        for  i  in range (len(s))  : 
            if s[i] not in k: 
                lst.append(s[i]) 
        return lst  
def getCoordinate(arr,line_count) : 
    ar = [] 
    Arr = []  
    _dictOfdata = [] 
    for i in range(len(arr) ) :  
        ar.append(getString(arr[i])) 
    for i in range(line_count)  : 
         Arr.append(ar[i][0])      
         _dictOfdata.append(ar[i][0] , [ar[i][1]])   
    return _dictOfdata   
def checkEmpty(s) : 
    for x in  (s) : 
            if len(x) == 0 :  
                return True  
                break  
def codeLength(_s,pos) :  
    _s = mergeNumber(_s)   
    s = [] 
    _DICT = {}
    _stack = [] 
    temp = [] 
    k =  0
    for i in range (pos+1 , len(_s)) : 
        temp.append(_s[i])  
        if(_s[i] =='|') :  
            pos = i  
            break 
        if(_s[i] == ';')  : 
            s.append(temp) 
            temp =[]
    if len(temp) != 0  : 
            s.append(temp)
    temp =[]
    for i in range(len(s)) : 
        if(s[i][1].isalpha() or s[i][1].isdigit()) :
            lstr= s[i][0]+s[i][1] 
        else : 
            lstr = s[i][0]
        for j in range(2,len(s[i])) :  
            if(s[i][j].isdigit()) :
                temp.append(s[i][j]) 
        _DICT.__setitem__(lstr,temp)
        temp=[]  
    return (_DICT ,pos )
def dup(s) : 
    s = list(dict.fromkeys(s)) 
    return s 
def Iversion(s) : 
    _dict ={}
    count = 1 
    j = 0 
    for i in range (len(s)-2)  :   
        if(j < len(s)):
            _dict.__setitem__(count , [tuple(s[j]), tuple(s[j+1])])  
        j += 2
        count += 1  
    return _dict   
def distance(s) :  
    _dict ={}
    count = 1 
    j=0
    for i in range (len(s)-2)  :   
        if(j < len(s)) :
            _dict.__setitem__(count , math.sqrt((float(s[j][0])-float(s[j+1][0]))**2 +(float(s[i][1])-float(s[i+1][1]))**2 ))  
            j+=2
            count += 1  
    return _dict     
def mergr(s) : 
    s= Mer2(s)
    k =[]
    for i in range(len(s)) : 
        if(s[i] == '-' and s[i+1].isdigit() ) :  
           s[i] = s[i]+s[i+1] 
           k.append(i+1)
    if(len(k) > 0 )  : 
        for i in range (len(k)) :  
            del(s[k[i]])
    else : pass 

    return s
def ForcesAtPoint(_s,pos) : 
    _s = _s.strip()
    s = [] 
    _DICT = {}
    _stack = [] 
    temp = [] 
    k =  0
    #_s = mergr(_s)
    if(len(_s) != 0):   
        _s = mergr(_s)
        print(_s)
        for i in range (pos+1 , len(_s)) : 
            temp.append(_s[i])  
            if(_s[i] == ';')  : 
                s.append(temp) 
                temp =[]
        if len(temp) != 0  : 
                s.append(temp)
        print(s)
        temp =[]
        for i in range(len(s)) : 
            if(s[i][1].isalpha() or s[i][1].isdigit()) :
                lstr= s[i][0]+s[i][1] 
            else : 
                lstr = s[i][0]
            for j in range(2,len(s[i])) :  
                if(s[i][j].isdigit() or '-' in s[i][j]) :
                    temp.append(s[i][j]) 
            _DICT.__setitem__(lstr,temp)
            temp=[]  
    return (_DICT ,pos )
def Forces(_s,_A,pos) : 
    _s = mergeNumber(_s)   
    s = [] 
    _DICT = {}
    _dict = _A
    _stack = []
    for i in range (pos+1 , len(_s)) : 
        s.append(_s[i]) 
    if (len(s) != 0 ) : 
        while(len(s) != 0 ) :  
            count =0   
            temp = []
            while(count < 4 ) :  
                temp.append(s.pop()) 
                count += 1 
            temp = temp[::-1]
            _stack.append(temp) 
        s = _stack 
        arr = [] 
        arr1=[] 
        arr2=[]
        arr3=[]
        for i in range(len(_dict)) : 
            arr.append(0) 
            arr1.append(0) 
            arr2.append(0)
            arr3.append(0)
        _dictionary={'Fs':arr,'Fa':arr1,'Fd':arr2,'Md':arr3 }

        for i in range (len(_stack) ) : 
            _stack[i][1] = [(_stack[i][1])] 
        for i in range (len(_stack) ) :   
           k = str(_stack[i][0]) + str(_stack[i][1] )
           _DICT.__setitem__(k,_stack[i][3])  
           (_dictionary[str(_stack[i][0])])[int(_stack[i][1][0])-1] = int(_DICT[k])
        return(_dictionary) 
    else : 
        arr = [] 
        arr1=[] 
        arr2=[]
        arr3=[]
        for i in range(len(_dict)) : 
            arr.append(0) 
            arr1.append(0) 
            arr2.append(0)
            arr3.append(0)
        _dictionary={'Fs':arr,'Fa':arr1,'Fd':arr2,'Md':arr3 } 
        return (_dictionary)
def middle(s) : 
    _dict ={}
    count = 1 
    j=0
    for i in range (len(s)-2)  :  
        if(j<len(s)) :
             _dict.__setitem__(count , [str((float(s[j][0])+float(s[j+1][0]))/2) ,str((float(s[j][1])+float(s[j+1][1]))/2) ]  )
        j+=2
        count += 1   
    return _dict  
def checkdup(Paircooedinate) :     
    s = set() 
    res = []  
    k = []
    for i in range (len(Paircooedinate)) :
        k.append(tuple(Paircooedinate[i])) 
    Paircooedinate = k 
    for i in range(len(Paircooedinate)) :
        if(Paircooedinate[i] not in s ) : 
            res.append(Paircooedinate[i]) 
            s.add(Paircooedinate[i])  
    k =[]
    for i in range (len(res)) :
        k.append(list(res[i])) 
    res = k 
    res = res[::-1]  
    return res  
def check(s,s1) :   
    _dict ={}
    for i in range(len(s))  :  
            _dict.__setitem__(tuple([s[i],s1[i]]) , i+1) 
    return _dict
def testdistacne(s) :  
    _dict ={} 
    stack =[]  
    count = 0  
    key = 0
    s =s[::-1]
    while(len(s) != 0 ) :  
        count = 0 
        while( count != 2  ) : 
            stack.append(s.pop()) 
            count +=1 
        key+=1
        distance = 0 
        distance = math.sqrt((int(stack[0][0])-int(stack[1][0]))**2+(int(stack[0][1])-int(stack[1][1]))**2) 
        stack =[]
        _dict.__setitem__(key,distance)
    return _dict
def retangle(s) : 
    _dict ={}
    _dict1 ={} 
    newdict=[]
    count = 1 
    _arr = []
    for i in range (len(s)-1)  :  
        k = [s[i+1][0],s[i][1]]
        _arr.append(s[i])  
        _arr.append(k)
    
    _dict = testdistacne(_arr) 
    _dict1 = distance(s)
    for i in range (1,len(_dict)+1) : 
       newdict.append(_dict[i]/_dict1[i])   
    return newdict
def Node(s) :  
    _dict={}
    for i in range(len(s)) : 
        _dict.__setitem__(i+1 , s[i]) 
    return _dict  
def mertext(s) : 
    str1=""
    k= (mergeNumber(s)) 
    k = k[1:len(s)-1]
    for i in range (len(k)) : 
        str1 = str1+ str(k[i]) + ','   
    return str1[:len(str1)-1]
def altho(s) :  
    _deque = deque() 
    Coordinate ='' 
    Val = []
    for i in range ( len(s)) : 
        if ('INPUT'  not in s[i])  :  
            _deque.append(s[i])  
    while(len(_deque) != 0 ) : 
        k = _deque.popleft()   
        if(k != '}'  ) : 
            Coordinate += k 
        elif (k == '}' )  : 
           Val.append(Coordinate) 
           Coordinate ='' 
    return Val
def checkgrip(s) : 
    grip=[]
    for i in s : 
        if (len(i) == 3 )  : 
            grip.append(i) 
    return grip
def test(s) :  
    _char = []  
    _eval = []
    _crash = [] 
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = "" 
    for i in alphabet : 
        _str += i  
    _str = _str + "0123456789"+_str.upper()+'*/+-()'
    while(s) : 
        if s[0] in _str : 
            TakeNumber = s[0] 
            s = s[1:] 
            while(s and s[0] in _str)  : 
                TakeNumber += s[0] 
                s = s[1:] 
            _char.append(TakeNumber) 
            if s : 
                _crash.append(s[0]) 
                s = s[1:] 
        else : 
            _char.append(s[0]) 
            s = s[1:]  
    _stack =[]  

    k = ['cos','sin','tan']
    count  = 0 
    for i in range(len(_char)) :  
        for j in range(len(k)) : 
            count = _char[i].find(k[j]) 
            if(count != -1 ) : break  
           
    print(count) 
    _eval = []
    _alpha =''
    angle =''
    if(count != 0) :  
        for i in range(len(_char)) :      
                j = count 
                while(_char[i][j] != '(') : 
                    _alpha+= _char[i][j] 
                    j+=1
                count = j  
                j = count+1
                while( _char[i][j] != ')') :  
                    angle +=  _char[i][j] 
                    j+=1 
                _eval.append([_alpha,angle])
    pass 
def changrCoor(s) : 
    for i in range(len(s)) : 
       if(len(s[i])== 3 ) : 
           s[i].remove(s[i][2])
    return s 
def codeConst(_s,pos,Paircoordinate):  
    _dd=(Node(Paircoordinate))
    print(_dd)
    _s = _s.strip()
    s = [] 
    _DICT = {}
    _stack = [] 
    temp = [] 
    k =  0
    if(len(_s) != 0): 
        _s = mergeNumber(_s) 
        for i in range (pos+1 , len(_s)) : 
            temp.append(_s[i])  
            if(_s[i] =='|') :  
                pos = i  
                break 
            if(_s[i] == ';')  : 
                s.append(temp) 
                temp =[]
        if len(temp) != 0  : 
                s.append(temp)
        temp =[]
        for i in range(len(s)) : 
            if(s[i][1].isalpha() or s[i][1].isdigit()) :
                lstr= s[i][0]+s[i][1] 
            else : 
                lstr = s[i][0]
            for j in range(2,len(s[i])) :  
                if(s[i][j].isdigit()) :
                    temp.append(s[i][j]) 
            _stack.append(lstr)

            _DICT.__setitem__(lstr,temp)
            temp=[]   
        for i in range(len(_stack)) : 
            for j in range(len(_DICT[_stack[i]])) : 
                _DICT[_stack[i]][j] = _dd[int( _DICT[_stack[i]][j])]
    return _DICT  
def LinkPoinr(s,pair) : 
    pos = 0
    k = Node(pair)  
    pofix = [] 
    stack  = []      
    count =  0 
    s = mergeNumber(s)  
    alphabet = [chr(chnum) for chnum in list (range(ord('a'),ord('z') + 1))]  
    _str = ""  
    for i in alphabet : 
        _str += i  
    _str = _str + "0123456789"+_str.upper()+"*/+^."
    for i in range(pos , len(s)) :   
        _tuple=()  
        _stack = [] 
        if(s[i] in _str or len(s[i])>1) : 
            stack.append(s[i]) 
        elif (s[i] == ';'or s[i] =='-') : 
            while(len(stack) != 0) : 
                 _stack.append(stack.pop())  
            pofix.append(_stack[::-1]) 
        else : continue
    if (len(stack) != 0 )      : 
        while(len(stack) != 0) : 
            _stack.append(stack.pop())  
        pofix.append(_stack[::-1])  
    for i in range(len(pofix)) : 
        if (len(pofix[i]) == 1) : 
            l=k[int(pofix[i][0])] 
            pofix[i]=l
    return (pofix) 
def result(s , dof ) :   
        _dict = {}
        if(dof  == 2 ) :  
           s = s[::-1] 
           count = 1 
           while(len(s) != 0 ) :  
               r1 = s.pop() 
               r2 = s.pop() 
               _dict.__setitem__(count , [r1,r2])  
               count +=1  
        else : 
            s = s[::-1] 
            count = 1 
            while(len(s) != 0 ) :  
               r1 = s.pop() 
               r2 = s.pop()  
               r3 = s.pop()
               _dict.__setitem__(count , [r1,r2,r3])  
               count +=1  
        return(_dict) 
def getmiddldeval(s1,s2) :   
    return([(s1[0]+s2[0])/2,(s1[1]+s2[1])/2])

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
def rotate90(s,pair)  :     
    deque    
    stack =[]
    k = LinkPoinr(s,pair)
    K =  LinkPoinr(s,pair)
    for i in range(len(k)) : 
        for j in range(len(k[i])) : 
            k[i][j] = float(k[i][j])
            K[i][j] = float(K[i][j])
    i =0 ; 
    j = 1 ;  
    mid =[]
    while(j < len(k)) : 
        mid.append(getmiddldeval(k[i],k[j])) 
        i+=2 
        j+=2
  
    k = k[::-1]  
    i = 0 
    count = 0 
    temp = k 
    _stack =[]
    while(len(k) != 0 ) : 
        count = 0 
        while(count < 2 ) :
            stack.append(getmiddldeval(k.pop(),mid[i] ) ) 
            count += 1 
        i+=1 
    for i in range(len(stack)) : 
            x,y = rotate((K[i]),(stack[i]),90)
            k.append((x,y)) 
    return k 
    

            
if __name__ == "__main__" : 
    f1 = function 
    f2  = function 
    list1 = [] 
    list1.append(function.getindict(f1,"12,12"))    
    list1.append(function.getindict(f1,"13,L"))   
    """#s = checkandSplit(['1','1','2'])  
    #print(_charsym(['P*Q-1','K*Q']))    
    ls = ["abcs,asdsad,asdasd"]  
    #print(list1) 
    _dict = {'k':'2','q':'3','l':'2'} 
    lst = ['q'] 
    LL = [['1','k'], ['1','k*l']]
    k = '?L=2,k=3,z=5,q=2 ?(1,k);(1,k*q);(2,3)|L(1)=[200]|(j=2)|(1,2)|F(x)=[200,100,200];F(y)=[200,30,900];M=[200,200,300]|Fs(1)=200'
    print(declaration(k)[1])  
    pos = declaration(k)[1]
    print(splitText(k,pos)) 
    pos = splitText(k,pos)[1] 
    print(codeLength(k,pos)) 
    pos = codeLength(k,pos)[1]
    print(Momentcode(k,pos))  
    print(pos)
    pos = Momentcode(k,pos)[1] 
    print(gripcode(k,pos)  )
    pos = gripcode(k,pos)[1] 
    print(pos) 
    __A = [['1','2'] ,['2','3'],['3','9'],['3','1'] ] 
    _A =[2,2,3,2,1,2,2,2,1]
    _a = [['1', '2'], ['2', '2'], ['2', '3'], ['3', '3'], ['3', '9'], ['0', '9']]
    print(ForcesAtPoint(k,pos)) 
    pos = ForcesAtPoint(k,pos)[1]
    #print(Forces(k,__A ,pos))
    #print(middle(__A))
    print(distance(__A))
    print(retangle(__A)) 
    """ 
    """print(altho(['INPUT COORDINATE{','(1,2);(2,3)','(1,2);(4,1)','}', 'INPUT LENGTH {', '', '}'])) 
    print(ForcesAtPoint('',-1))
    print(checkgrip([['1','2','O']]))
    print(declaration('L=100;k=300')) """
    k=[['l','l-q','l/q'],['l*q']] 
    _dict = {'l':'200','q':'300'} 
    #print(test('L*cos(45)')) 
    #print(codeConst('const_x=[2,1,3];const_y=[1,2,3]',-1, [['1','2'] ,['2','3'],['3','9'],['3','1'] ]))    
    #print(Node([['1','2'] ,['2','3'],['3','9'],['3','1'] ])) 
    #k = (LinkPoinr('(1)-(2);(2)-(3)',[['1','2'] ,['2','3'],['3','9'],['5','6]])) 
    #print(Iversion(k)) 
    #print(mergeNumber('F(x)=[0,0,0];F(y)=[0,0,-2000];M=[0,0,0]'))
    print(ForcesAtPoint('F(x)=[0,0,0];F(y)=[0,0,-2000];M=[0,0,0]',-1)) 
    print('2000'.isdigit())  
    print(mergr('F(x)=[0,0,0];F(y)=[0,0,-2000]')) 
    print(result([1,2,3,43],2)) 
    print(Forces('',['1','2'] , -1 )) 
    k = (splitText('(1,2);(2.5,4)',0)) 
    print(rotate90('(1,2);(2,3);(2,3);(5,6)',[['1','2'] ,['2','3'],['2','3'],['5','6']]))
    print(distance([['1','2'] ,['2','3'],['2','3'],['5','6']]))


