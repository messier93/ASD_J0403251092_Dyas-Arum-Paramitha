# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# =========================
# Insertion Sort (Descending)
# =========================

def insertionSort(data):
    for index in range(1,len(data)):

        currentValue = data[index]
        position = index

        while position > 0 and data[position-1] < currentValue:
            data[position] = data[position-1]
            position = position-1
            data[position] = currentValue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)

#Output [93, 77, 55, 54, 44, 31, 26, 20, 17]