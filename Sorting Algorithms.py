

compMs = 0
compQs = 0

# Comparison Counts Given After the Sorted Array 
def InsertionSort(file):
    compIs = 0
##    fileName = open('10_Random.txt', 'r')
##    fileName = open('10_Reverse.txt', 'r')
##    fileName = open('10_Sorted.txt', 'r')
##    fileName = open('100_Random.txt', 'r')
##    fileName = open('100_Reverse.txt', 'r')
##    fileName = open('100_Sorted.txt', 'r')
##    fileName = open('1000_Random.txt', 'r')
##    fileName = open('1000_Reverse.txt', 'r')
    fileName = open('1000_Sorted.txt', 'r')
    num = fileName.read().splitlines()
    arr = [int(j) for j in num]
    for item in range(1, len(arr)):
        val = arr[item]
        idx = item
        while idx > 0:
            if val < arr[idx-1]:
                arr[idx] = arr[idx-1]
                idx-=1
                compIs +=1
            else:
                compIs +=1
                break
        arr[idx] = val
    return  compIs ,'<-- Comparison'

def MergeSort(file):
    global compMs
##    fileName = open('10_Random.txt', 'r')
##    fileName = open('10_Reverse.txt', 'r')
##    fileName = open('10_Sorted.txt', 'r')
##    fileName = open('100_Random.txt', 'r')
##    fileName = open('100_Reverse.txt', 'r')
##    fileName = open('100_Sorted.txt', 'r')
##    fileName = open('1000_Random.txt', 'r')
##    fileName = open('1000_Reverse.txt', 'r')
    fileName = open('1000_Sorted.txt', 'r')
    num = fileName.read().splitlines()
    arr = [int(j) for j in num]
    mergDiv(arr)
    return compMs,'<-- Comparison'

def mergDiv(arr):
    if len(arr) < 2:
        return arr
    k = int((len(arr)) / 2)
    lft = arr[:k]
    rgt = arr[k:]
    return mrg(mergDiv(lft), mergDiv(rgt))

def mrg(lft, rgt):
    array = []
    i=j=0
    global compMs
    while i < len(lft) and j < len(rgt):
        if lft[i] < rgt[j]:
            array.append(lft[i])
            i+=1
            compMs+=1          
        else:
            array.append(rgt[j])
            j+=1
            compMs+=1
    array += lft[i:]
    array += rgt[j:]

    return array


def QuickSort(file):
    global compQs 
##    fileName = open('10_Random.txt', 'r')
##    fileName = open('10_Reverse.txt', 'r')
##    fileName = open('10_Sorted.txt', 'r')
##    fileName = open('100_Random.txt', 'r')
##    fileName = open('100_Reverse.txt', 'r')
##    fileName = open('100_Sorted.txt', 'r')
##    fileName = open('1000_Random.txt', 'r')
##    fileName = open('1000_Reverse.txt', 'r')
    fileName = open('1000_Sorted.txt', 'r')
    num = fileName.read().splitlines()
    arr = [int(j) for j in num]
    qs(arr, 0, len(arr)-1)
    return  compQs ,'<-- Comparison'

def qs(arr, fst, lst):
    if fst < lst:
        split = Partition(arr, fst, lst)
        qs(arr, fst, split-1)
        qs(arr, split+1, lst)


def Partition(arr, fst, lst):
    global compQs
    fstNum = arr[fst]
    add = fst+1
    fileName = fst
    for item in range(add, lst+1):
        compQs+=1
        if arr[item] < fstNum:
            fileName+=1
            arr[fileName], arr[item] = arr[item], arr[fileName]
    arr[fst], arr[fileName] = arr[fileName], arr[fst]
    
    return fileName
	

print '\nInsertionSort \n', InsertionSort(file)
print '\nMergeSort \n', MergeSort(file)
print '\nQuickSort \n', QuickSort(file)	
	
