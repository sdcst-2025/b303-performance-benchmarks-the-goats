import time
import json
def sortcode():
    n = input('Enter an integer:')
    f = open(f"{n}tbest.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.time()
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.time()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Best took {elapsed:.100f} seconds")

    f = open(f"{n}tdata.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.time()
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.time()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Random took {elapsed:.100f} seconds")

    f = open(f"{n}tworst.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.time()
    #print(d.data)
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.time()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Worst took {elapsed:.100f} seconds")

sortcode()