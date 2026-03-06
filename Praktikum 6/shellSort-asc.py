# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# =========================
# Shell Sort (Asccending)
# =========================

def shellSort(data):
    sublistcount = len(data)//2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data,startposition,sublistcount)

        print("After increments of size ",sublistcount,"The list is",data)
           
        sublistcount = sublistcount//2

def gapInsertionSort(data,start,gap):
    for i in range(start+gap,len(data),gap):

        currentValue = data[i]
        position = i

        while position >= gap and data[position-gap]>currentValue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentValue

data = [54,26,93,17,77,31,44,55,20]
shellSort(data)
print(data)

#Output [93, 77, 55, 54, 44, 31, 26, 20, 17]