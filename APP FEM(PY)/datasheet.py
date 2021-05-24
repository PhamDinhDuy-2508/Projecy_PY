import csv
from csv import writer 
import numpy as np 
import Algorithms
def DataOfMaterial() :
    with open('database.txt' , mode='r') as csv_file: 
        Arr = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 
        print('Name of Material \t' ,'Incides possion\t' ,  'Incides Material\t' , 'cross-section area\t' , ) 
        arr = np.genfromtxt('database.txt',dtype= str)    
        for row in csv_reader:
                line_count += 1  
        Arr = Algorithms.getNameofMaterial(arr , line_count) 
    return Arr  
def GetDict() : 
    with open('database.txt' , mode='r') as csv_file: 
        Arr = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 
        arr = np.genfromtxt('database.txt',dtype= str)    
        for row in csv_reader:
                line_count += 1  
        Arr = Algorithms.GetNameMaterialDICt(arr , line_count) 
    return Arr  
def Update(_dict) :  
    with open('database.txt' , mode='r') as csv_file: 
        _Arr = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 
        #print('Name of Material \t' ,'Incides possion\t' ,  'Incides Material')
        arr = np.genfromtxt('database.txt',dtype= str)    
        for row in csv_reader:
                line_count += 1  
        Arr = Algorithms.getNameofMaterial(arr , line_count)  
        find = Algorithms.search(Arr , 0 , len(Arr)  , _dict.key())  
        _Arr = Algorithms.GetNameMaterialDICt(arr , line_count) 
        if(find != -1 )  : 
            _Arr[Arr[find]][0]= (_dict[Arr[find]])[0]  
            _Arr[Arr[find]][1]= (_dict[Arr[find]])[1]  
            readdata = [row for row in csv.DictReader(csv_file)] 
            readdata[0][Arr[find]] = _dict[Arr[find]][0]
            readdata[1][Arr[find]] = _dict[Arr[find]][1]
        else :  
            pass 
    pass 
def getPairCoordinate() :  
    with open('ex.txt' , mode='r') as csv_file: 
        Arr = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 
        arr = np.genfromtxt('ex.txt',dtype= str)    
        for row in csv_reader:
                line_count += 1 
        Arr = Algorithms.getCoordinate(arr , line_count)  
    return Arr 







