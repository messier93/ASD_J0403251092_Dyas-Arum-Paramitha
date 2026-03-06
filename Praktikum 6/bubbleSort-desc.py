# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# =========================
# Bubble Sort (Descending)
# =========================

def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        #jika elemen kanan lebih besar dari kirimaka tukar
        for i in range(passnum):
            if data[i]<data[i+1]: #ubah tanda agar mnjd terbalik
            #tukar dua data bersebalahan yg urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)

#Program 4
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    
    while passnum > 0 and exchanges:
        exchanges = False
        
        for i in range(passnum):
            # kondisi dibalik untuk descending
            if alist[i] < alist[i+1]:
                exchanges = True
                
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        
        passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]

shortBubbleSort(alist)

print(alist)

#Output [93, 77, 55, 54, 44, 31, 26, 20, 17]
