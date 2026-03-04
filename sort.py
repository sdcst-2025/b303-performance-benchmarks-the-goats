def sortcode():
    x = input('Enter an integer:')
    import f'{self.x}tdata.py' as d
    
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
    print(f"This took {elapsed} seconds")