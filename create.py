import time
import os
import random
class sorttest():
    def randsort(self):
        file = open(self.randname,'w')
        l = []
        for i in range(0,self.x):
            l.append(i)
        random.shuffle(l)
        file.write(f'{l}')
    def bestsort(self):
        file = open(self.bestname,'w')
        l =[]
        for i in range(0,self.x):
            l.append(i)    
        file.write(f'{l}')
    def worstsort(self):
        file = open(self.worstname, 'w')       
        l = []
        for i in range(0,self.x):
            l.append(i)  
        l.reverse()
        file.write(f'{l}')        
    """def sortcode(self):
        import data10000 as d

        start = time.time()
        #print(d.data)
        for k in range(len(d.data)):
            for j in range(k, len(d.data)):
                if d.data[k] > d.data[j]:
                    temp = d.data[k]
                    d.data[k] = d.data[j]
                    d.data[j] = temp
        end = time.time()
        elapsed = end - start
        print("\n\n")
        print(f"This took {elapsed} seconds")"""
    def __init__(self):
        self.x = int(input("Enter an integer: "))
        self.randname = f'{self.x}tdata.py'
        self.bestname = f'{self.x}tbest.py'
        self.worstname = f'{self.x}tworst.py'
        self.randsort()
        self.bestsort()
        self.worstsort()

x = sorttest()
# File should have 1 input that reads an integer
# generates 3 files: tdata<x>.py tbest<x>.py and tworst<x>.py where x is the integer
# each datafile will be importable so we can read the variable that is stored within it. 