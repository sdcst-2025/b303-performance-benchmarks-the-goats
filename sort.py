import time
import json
def bubble_sort():
    n = input('Enter an integer:')
    f = open(f"{n}tbest.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.perf_counter()
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.perf_counter()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Best bubble sort took {elapsed:.10f} seconds")

    f = open(f"{n}tdata.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.perf_counter()
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.perf_counter()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Random bubble sort took {elapsed:.10f} seconds")

    f = open(f"{n}tworst.py","r")
    importedb = f.readline()
    x = json.loads(importedb)
    
    start = time.perf_counter()
    #print(d.data)
    for k in range(len(x)):
        for j in range(k, len(x)):
            if x[k] > x[j]:
                temp = x[k]
                x[k] = x[j]
                x[j] = temp
    end = time.perf_counter()
    #f.write('sorted')
    elapsed = end - start
    print("\n\n")
    print(f"Worst bubble sort took {elapsed:.10f} seconds")

def heapify(arr, n, i):

    # Initialize largest as root
    largest = i

    # left index = 2*i + 1
    l = 2 * i + 1

    # right index = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build heap (rearrange vector)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):

        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def pigeonhole_sort(a):
    # size of range of values in the list 
    # (ie, number of pigeonholes we need)
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1

    # our list of pigeonholes
    holes = [0] * size

    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
    return a

def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

while True:
    which = input("Enter which sort method you want to use: ")
    if which == "bubble" or which =="Bubble":

        bubble_sort()

    elif which == "heap" or which =="Heap":

        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        heap_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Heap sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        heap_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Heap sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        heap_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Heap sort for worst data took {elapsed} seconds")

    elif which == "insertion" or which == "Insertion":

        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        insertion_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Insertion sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        insertion_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Insertion sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        insertion_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Insertion sort for worst data took {elapsed} seconds")

    elif which == "pigeon" or which == "Pigeon":
        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        pigeonhole_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Pigeon hole sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        pigeonhole_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Pigeon hole sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        pigeonhole_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Pigeon hole sort for worst data took {elapsed} seconds")

    elif which == "quick" or which == "Quick":
        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        lastPos = len(x)-1   
        start = time.perf_counter()
        sorted = quickSort(x,0,lastPos)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Quick sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        lastPos = len(x)-1  
        start = time.perf_counter()
        sorted = quickSort(x,0,lastPos)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Quick sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        lastPos = len(x)-1  
        start = time.perf_counter()
        sorted = quickSort(x,0,lastPos)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Quick sort for worst data took {elapsed} seconds")
   
    elif which =="radix" or which == "Radix":

        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        radixSort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Radix sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        radixSort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Radix sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        radixSort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Radix sort for worst data took {elapsed} seconds")

    elif which == "selection" or which == "Selection":
        
        num = int(input("Enter an integer: "))
        f = open(f"{num}tbest.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        selection_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Selection sort for best data took {elapsed} seconds")

        f = open(f"{num}tdata.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        selection_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Selection sort for random data took {elapsed} seconds")

        f = open(f"{num}tworst.py","r")
        importedb = f.readline()
        x = json.loads(importedb)
        start = time.perf_counter()
        selection_sort(x)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Selection sort for worst data took {elapsed} seconds")
    else:
        print("Invalid input, the options are: bubble, heap, insertion, pigeon, quick, radix, or selection.")